import pyes
import os
from models import *
from sqlalchemy import select
from downloader import download
import utils
import re

def index():
    mapping = {
        'document':{
            'type':'attachment',
            'fields':{
                "title" : { "store" : "yes" },
                "file" : { 
                     "term_vector":"with_positions_offsets", 
                     "store":"yes" 
                }
            }
        },
        'name':{
            'type':'string',
            'store':'yes',
            'boost':1.0,
            'index':'analyzed'
        },
        'long_name':{
            'type':'string',
            'store':'yes',
            'boost':1.0,
            'index':'analyzed'
        },
        'status':{
            'type':'string',
            'store':'yes',
        },
        'year':{
            'type':'integer',
            'store':'yes'
        },
        'read_by':{
            'type':'string',
            'store':'yes',
            'index':'analyzed'
        },
        'date_presented':{
            'type':'date',
            'store':'yes'
        },
        'bill_id':{
            'type':'integer',
            'store':'yes'
        },
        'id':{
            'type':'integer',
            'store':'yes'
        }
    }

    es = pyes.ES('localhost:9200')
    es.create_index_if_missing('bill-index')
    es.put_mapping('bill-type',
        {'bill-type':{
            '_id':{
                'path':'id'
            },
            'properties':mapping
            }
        },['bill-index'])
    es.refresh('bill-index')
    get_row = get_indexable_bills()
    for i in get_row:
        es.index(i,'bill-index','bill-type')
        es.refresh('bill-index')

def extract_bills():
    initdb()
    session = DBSession()

    revision = (session.query(BillRevision)
                .join((BillRevision.bill,Bill)).all()
                )
    
    for rev in revision:
        temp = {}
        rev_key = [ i for i in dir(rev) if not re.match('^_',i) ]
        bill_key = [ i for i in dir(rev.bill) if not re.match('^_',i) ]
        for key in rev_key:
            if key != 'metadata' and key != 'bill':
                temp[key] = getattr(rev,key)
        for key in bill_key:
            if key != 'metadata' and key!='id' and key!='bill_revs':
                temp[key] = getattr(rev.bill,key)
        yield temp

        
def get_indexable_bills():
    data = extract_bills()
    for item in data:
        temp = {}
        for key in item.keys():
            if key == 'url':
                full_path = download(item[key])
                if not full_path:
                    continue

                temp['document'] = pyes.file_to_attachment(full_path)
            else:
                temp[key] = item[key]
        print '%s:%s' % (temp['id'],temp['long_name'])
        yield temp

def extract_individual_bills(rev_id):
    initdb()
    session = DBSession()

    revision = (session.query(BillRevision).get(rev_id)
                )
    
    temp = {}
    rev_key = [ i for i in dir(revision) if not re.match('^_',i) ]
    bill_key = [ i for i in dir(revision.bill) if not re.match('^_',i) ]
    for key in rev_key:
        if key != 'metadata' and key != 'bill':
            temp[key] = getattr(revision,key)
    for key in bill_key:
        if key != 'metadata' and key!='id' and key!='bill_revs':
            temp[key] = getattr(revision.bill,key)
    return temp

def get_individual_indexable_bills(rev_id):
    bill = extract_individual_bills(rev_id)
    temp = {}
    for key in bill.keys():
        if key == 'url':
            full_path = download(bill[key])
            if not full_path:
                continue

            temp['document'] = pyes.file_to_attachment(full_path)
        else:
            temp[key] = bill[key]
    print '%s:%s' % (temp['id'],temp['long_name'])
    return temp

def index_individual_bill(rev_id):
    es = pyes.ES('localhost:9200')
    bill = get_individual_indexable_bills(rev_id)
    es.index(bill,'bill-index','bill-type')
    es.refresh('bill-index')

if __name__ == '__main__':
    index()
