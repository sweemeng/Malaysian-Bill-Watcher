import logging
import datetime
import cStringIO
import pyes
import PyRSS2Gen

from sqlalchemy import select
from sqlalchemy.sql import and_,func

from bottle import route, view, static_file, request, response

import models
import settings
import utils

log = logging.getLogger(__name__)

@route('/detail/<rev_id>/')
@view('detail')
def detail(rev_id):
    session = models.DBSession()
    rev = session.query(models.BillRevision).get(rev_id)
    return {'rev':rev}

@route('/')
@view('list')
def list_all():
    page_no = request.GET.get('page_no')

    session = models.DBSession()
    bills = (session.query(models.Bill)
             .join((models.Bill.bill_revs,
                    models.BillRevision))
             .order_by(models.BillRevision.update_date)
             .all())

    pages = utils.Pagination(settings.ITEM_PER_PAGE,
                             len(bills), page_no)
    bills = bills[pages.first:pages.last]
    return {'bills':bills,
            'pages':pages}

@route('/feeds/')
def feed():
    prefix = '://'.join(request.urlparts[:2])
    title = 'Malaysian Bill Watcher'
    link = prefix + '/'
    description = 'This is an app for Malaysian to see bill being passed by the Parliament'

    lastBuildDate = datetime.datetime.utcnow()
    
    session = models.DBSession()
    bills = (session.query(models.Bill)
             .join((models.Bill.bill_revs, models.BillRevision))
             .order_by(models.BillRevision.update_date)
             .all())

    items = []
    for bill in bills:
        _rev = bill.bill_revs[0]
        _title = bill.long_name
        _description = "year:%s \nstatus: %s" % (_rev.year,
                                                 _rev.status)
        _link = prefix + '/detail/%s/' % (_rev.id)
        _pubDate = _rev.update_date
        _guid = PyRSS2Gen.Guid(_link)
        item = PyRSS2Gen.RSSItem(title=_title, description=_description,
                                 link=_link, guid=_guid, pubDate=_pubDate)
        items.append(item)

    rss = PyRSS2Gen.RSS2(title=title, link=link, description=description,
                         items=items)
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
    session = models.DBSession()
    for res in result['hits']['hits']:
        id = res['_id']
        bill = session.query(models.BillRevision).get(id)
        if not bill:
            log.info('bill_revs record with %r not found.' % id)
            continue
        bill_list.append(bill)
    return {'bill':bill_list}

@route('/about/')
@view('about-us')
def about_us():
    return {}
