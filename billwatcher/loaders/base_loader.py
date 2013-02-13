# internal api
import scraper
import models
import indexer

# external library
import requests
import datetime

# New loader require that 
# 1) We now have multiple data source
# 2) Each data source will deal with different state, 
#    Parliament deal with reading approval,
#    AG Chambers deals with gazzette. 
# 3) So yeah, 2 different scraper   
# 4) For now we using the existing primary key
# 5) AGC need us to implement enforce date

class BaseLoader(object):
    def __init__(self):
        self.current_rev = None
        self.request_URL = ""
        self.request_parameter = {}
        self.pages = []
        
        self.indexer = indexer.Search()
        self.session = models.DBSession()
        # a transition table is to check that it is in the next state
        # just a validation tool
        self.transition = {
        }
   
    # Code need to be clear, list all parameter needed  
    def write_bill(self, name, long_name):
        bill = models.Bill(
            name=name,
            long_name=long_name
        )
        self.session.add(bill)
        self.session.flush()
    
    def write_revision(self, url, status, year, read_by=None, supported_by=None, date_presented=None):
        revision = models.BillRevision(
            url=url,
            status=status,
            year=year,
            read_by=read_by,
            supported_by=supported_by,
            date_presented=date_presented,
            update_date=datetime.datetime.now()
        )
        self.session.add(revision)
        self.session.flush()
    
    def index_entry(self, revision_id):
        self.indexer.inder_single(revision_id)
   
    # we will need to handle multiple page,  
    def fetch_site(self):
        request = requests.get(self.request_url,params)
        if request.status_Code != 200:
            raise Exception("Site raise a non 200 code")
        results = self.process_site(request.text)
        for result in results:
            yield result
          
    def process_site(self, page):
        raise NotImplementedError("This need to be implemented")

    def run(self):
        raise NotImplementedError("This need to be implemented")

