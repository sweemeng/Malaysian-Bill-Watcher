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
            if key != 'metadata':
                temp[key] = getattr(rev,key)
        for key in bill_key:
            if key != 'metadata':
                temp[key] = getattr(rev.bill,key)
        yield temp

        
def get_indexable_bills():
    data = extract_bills()
    for item in data:
        temp = {}
        for key in item.keys()[1:]:
            new_key = utils.get_keys(key)
            
            if new_key == 'url':
                full_path = download(item[key])
                if not full_path:
                    continue

                temp['document'] = pyes.file_to_attachment(full_path)
            else:
                temp[new_key] = item[key]

        yield temp

if __name__ == '__main__':
    index()
