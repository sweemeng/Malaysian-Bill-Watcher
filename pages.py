from bottle import route,view,static_file,request,response
from models import bills,bill_revs
from models import engine
from sqlalchemy import select
from sqlalchemy.sql import and_,func
import PyRSS2Gen
import settings

import datetime
import cStringIO
import pyes

@route('/detail/<id>/')
@view('detail')
def detail(id):
    bl = select([bills],bills.c.id == id)
    conn = engine.connect()
    
    result = conn.execute(bl)
    bill = result.fetchone()
    rev = select([bill_revs],bill_revs.c.bill_id == bill['id']).\
        order_by(bill_revs.c.year.desc())
    
    result = conn.execute(rev)
    revision = result.fetchall()
    return dict(bill=bill,revision=revision)

@route('/')
@view('list')
def list_all():
    print request.GET.keys()
    if request.GET.get('page_no'):
        page_no = int(request.GET.get('page_no'))
    else:
        page_no = 1
    first = (page_no - 1)  *  settings.ITEM_PER_PAGE + 1
    last = settings.ITEM_PER_PAGE * page_no
    bl = select([bills,bill_revs],and_(
        bills.c.id==bill_revs.c.bill_id,
        bills.c.id>=first,bills.c.id<=last
        )
    ).order_by(bill_revs.c.update_date)
    conn = engine.connect()
    result = conn.execute(bl)
    bill = result.fetchall()

    cnt = select([bills])
    result = conn.execute(cnt)
    count = result.fetchall()
   
    page_list = range(len(count) / 5)
    page_list = [i+1 for i in page_list]
    return dict(bill=bill,page_list=page_list,page_no=page_no,
        next_page=page_no+1,prev_page=page_no-1)
    
@route('/css/<filename>')
def server_css(filename):
    return static_file(filename,root='./css/')

@route('/feeds/')
def feed():
    prefix = '://'.join(request.urlparts[:2])
    title = 'Malaysian Bill Watcher'
    link = prefix+'/'
    description = '''
        This is an app for Malaysian to see bill being passed by the Parliament
    '''
    lastBuildDate = datetime.datetime.utcnow()
    
    li = []
    bls = select([bills,bill_revs],bills.c.id==bill_revs.c.bill_id).\
        order_by('update_date')
    conn = engine.connect()
    result = conn.execute(bls)
    bill = result.fetchall()    
    for i in bill:
        i_title = i['long_name']
        i_description = "year:%s \nstatus: %s" % (i['year'],i['status'])
        i_link = prefix+'/detail/%s/' % (i['bill_id'])
        i_pubDate = i['update_date']
        i_guid = PyRSS2Gen.Guid(i_link)
        itm = PyRSS2Gen.RSSItem(title=i_title,description=i_description,
            link=i_link,guid=i_guid,pubDate=i_pubDate)
        li.append(itm)
    rss = PyRSS2Gen.RSS2(title=title,link=link,description=description,
        items = li)
    output = cStringIO.StringIO()
    rss.write_xml(output)
    response.content_type = 'application/rss+xml'
    return output.getvalue()

@route('/search/')
@view('search')
def search():
    es = pyes.ES('127.0.0.1:9200') 
    query_string = request.GET.get('query')
    query = pyes.StringQuery(query_string)
    result = es.search(query=query)
    bill = []
    for res in result['hits']['hits']:
        source = res['_source']
        temp = {}
        for k in source.keys():
            if k != 'document':
                temp[k] = source[k]
        bill.append(temp)
    print bill
    return dict(bill=bill)
