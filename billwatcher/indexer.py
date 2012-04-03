import pyes
import os
from models import *
from sqlalchemy import select
from downloader import download
import utils
import re
import time


class Search(object):
    def __init__(self,host,index,map_name,mapping=None,id_key=None):
        self.es = pyes.ES(host)
        self.index = index
        self.map_name = map_name
        self.mapping = mapping
        self.id_key = id_key

    def create_index(self):
        self.es.create_index_if_missing(self.index)
        if self.mapping:
            if self.id_key:
                self.es.put_mapping(self.map_name,{
                    self.map_name:{
                        '_id':{
                            'path':self.id_key
                        },
                        'properties':self.mapping}
                    },[self.index])

            else:
                self.es.put_mapping(self.map_name,{
                    self.map_name:{
                        'properties':self.mapping
                    }
                },[self.index])
        self.es.refresh(self.index)

    def index_item(self,item):
        self.es.index(item,self.index,self.map_name)
        self.es.refresh(self.index)


def convert_to_document(revision):
    temp = {}
    rev_key = [ i for i in dir(revision) if not re.match('^_',i) ]
    bill_key = [ i for i in dir(revision.bill) if not re.match('^_',i) ]
    for key in rev_key:
        if key != 'metadata' and key != 'bill':
            temp[key] = getattr(revision,key)
    for key in bill_key:
        if key != 'metadata' and key!='id' and key!='bill_revs':
            temp[key] = getattr(revision.bill,key)
    
    full_path = download(temp['url'])
    if full_path:
        temp['document'] = pyes.file_to_attachment(full_path)

    return temp

def initial_index():
    host = '127.0.0.1:9200'
    index = 'bill-index'
    map_name = 'bill-type'
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
   
    search = Search(host,index,map_name,mapping)
    search.create_index()

    initdb()
    session = DBSession()

    revision = (session.query(BillRevision)
                .join((BillRevision.bill,Bill)).all()
                )

    for rev in revision:
        temp = convert_to_document(rev)
        search.index_item(temp)
        time.sleep(5)

def index_single(rev_id):
    host = '127.0.0.1:9200'
    index = 'bill-index'
    map_name = 'bill-type'

    initdb()
    session = DBSession()

    revision = (session.query(BillRevision).get(rev_id)
                )
    temp = convert_to_document(revision)
    search = Search(host,index,map_name)
    search.index_item(temp)
   

if __name__ == '__main__':
    initial_index()
