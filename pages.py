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

import utils
        

@route('/detail/<rev_id>/')
@view('detail')
def detail(rev_id):
    bls = select([bills,bill_revs],
        and_(
            bill_revs.c.id == rev_id,
            bill_revs.c.bill_id==bills.c.id
        )
    ).apply_labels()

    conn = engine.connect()
    
    result = conn.execute(bls)
    bl = result.fetchone()
    
    bill = utils.get_bill(bl) 

    revs = select([bill_revs],bill_revs.c.bill_id == bill.bill_id).\
        order_by(bill_revs.c.year.desc())
    
    result = conn.execute(revs)
    revision = result.fetchall()
    
    return dict(bill=bill,revision=revision)

@route('/')
@view('list')
def list_all():
    page_no = request.GET.get('page_no')

    bl = select([bills,bill_revs],and_(
        bills.c.id==bill_revs.c.bill_id,
        )
    ).order_by(bill_revs.c.update_date).apply_labels()


    conn = engine.connect()
    result = conn.execute(bl)
    bill_list = result.fetchall()
    
    bill = []

    for item in bill_list:
        bill.append(utils.get_bill(item))        

    bill_total = len(bill_list)
    pages = utils.Pagination(settings.ITEM_PER_PAGE,bill_total,page_no)
    bill = bill[pages.first:pages.last]

    return dict(bill=bill,pages=pages)
    

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
        order_by('update_date').apply_labels()
    conn = engine.connect()
    result = conn.execute(bls)
    bill = result.fetchall()    
    for i in bill:
        i_bill = utils.get_bill(i)
        i_title = i_bill.long_name
        i_description = "year:%s \nstatus: %s" % (i_bill.year,i_bill.status)
        i_link = prefix+'/detail/%s/' % (i_bill.id)
        i_pubDate = i_bill.update_date
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
    bill_list = []
    conn = engine.connect()
    for res in result['hits']['hits']:
        id = res['_id']
        bls = select([bills,bill_revs],
            and_(
                bill_revs.c.id == id,
                bill_revs.c.bill_id==bills.c.id
            )
        ).apply_labels()

        conn = engine.connect()
    
        result = conn.execute(bls)
        bl = result.fetchone()
        if not bl:
            print id
            continue 
        bill = utils.get_bill(bl) 
        bill_list.append(bill)

    return dict(bill=bill_list)


@route('/js/<filename>')
def js_view(filename):
    return static_file(filename,root='js/')

@route('/pdf/<filename>')
def js_view(filename):
    return static_file(filename,root='files/')
