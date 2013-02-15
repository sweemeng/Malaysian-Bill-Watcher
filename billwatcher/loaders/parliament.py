from loaders.base import BaseLoader
from scrapers.parliament import MyTable
import requests



class ParliamentLoader(BaseLoader):
    def __init__(self):
        self.request_url = 'http://www.parlimen.gov.my/bills-dewan-rakyat.html'

    def process_site(self, page):
        parser = MyTable(page)
        result = parser.extract()
        return result

    def run(self):
        processor = self.fetch_site()
        for line in processor:
            bill = self.write_bill(line['kod']['kod_name'], line['tajuk'])
            revision = self.write_revision(
                bill.id,
                line['kod']['kod_path'], 
                line['status'],
                line['tahun'],
                line['Dibentang Oleh'],
                line['Diluluskan Pada']
            )
            self.index_entry(revision.id)
