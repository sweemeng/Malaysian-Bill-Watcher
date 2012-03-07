import logging
import datetime

from bottle import route, request

import models

log = logging.getLogger(__name__)

@route('/api/single/',method='GET')
def single_item():
    id = request.GET.get('id')
    session = models.DBSession()
    bill = session.query(models.Bill).get(id)
    data = serialize_bill(bill)
    return data

@route('/api/all/',method='GET')
def all_item():
    session = models.DBSession()
    bills = session.query(models.Bill).all()
    data = map(serialize_bill, bills)
    return {'data':data}

def serialize_bill(bill):
    revision = map(serialize_revision, bill.bill_revs)
    return {'id':bill.id,
            'name':bill.name,
            'long_name':bill.long_name,
            'revision':revision}

# This is more verbose and dummier
def serialize_revision(rev):
    data = {'id':rev.id,
            'url':rev.url,
            'status':rev.status,
            'year':rev.year,
            'read_by':rev.read_by,
            'supported_by':rev.supported_by,
            'bill_id':rev.bill_id}

    try:
        data['create_date'] = rev.create_date.strftime('%d/%m/%Y %H:%M:%s')
    except AttributeError:
        data['create_date'] = None

    try:
        data['update_date'] = rev.update_date.strftime('%d/%m/%Y %H:%M:%s')
    except AttributeError:
        data['update_date'] = None

    try:
        data['date_presented'] = rev.date_presented.strftime('%d/%m/%Y')
    except AttributeError:
        data['date_presented'] = None
    return data

