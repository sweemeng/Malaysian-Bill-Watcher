import pyes
import os
from models import bills,bill_revs,engine
from sqlalchemy import select
from downloader import download
import utils

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

def get_indexable_bills():
    revision = select([bill_revs,bills],bill_revs.c.bill_id==bills.c.id).apply_labels()
    conn = engine.connect()
    result = conn.execute(revision)
    data = result.fetchall()
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
