#!/usr/bin/env python
import re
import sys
import requests
import json
import bs4
# Bros
import base64

TARGET_URL = 'http://www.parlimen.gov.my'
MRBILLS = TARGET_URL + '/bills-dewan-rakyat.html'

file_rule = re.compile("loadResult\('(.*)','(.*)'\)")

def doReq():
    params = {'uweb':'dr'}
    print "Requesting latest bills..."
    r = requests.get(MRBILLS, params=params)
    if r.status_code != 200:
        sys.exit('Connection error, HTTP %d' % r.status_code)
    print 'Got it, you lucky brat!'
    mytable = MyTable(r.text)
    print 'Extracting...'
    data = mytable.extract()
    

class MyTable(object):
    def __init__(self, html):
        self.html = bs4.BeautifulSoup(html, 'lxml')
        self.total_row = 0
        # Count drabooola
        self.count = 0

    @property
    def table(self):
        return self.html.find("table", {"id": "mytable"})

    def _extract_row(self, row):
        self.count += 1
        print 'Processing %d out of %d files' % (self.count, self.total_row)

        cols = row.findChildren('td')
        kod = cols[0].find('a')
        kod_name = kod.text.strip()
        kod_fileinfo = kod['onclick'].strip()
        tahun = cols[1].text.strip()
        tajuk = cols[2].text.strip()
        status_col = cols[3]
        status_code = status_col.find('div', {'class':'parent'}).text.strip()
        status_table = status_col.find('table')
        status_rows = status_table.find_all('tr')
        # I assumed the repeated bendang is a bug
        bendang = status_rows[2].find_all('td')[2].text.strip()
        if not bendang:
            bendang = status_rows[4].find_all('td')[2].text.strip()
                
        status = {'status_code': status_code,
                  'Bacaan Pertama Pada': status_rows[0].find_all('td')[2].text.strip(),
                  'Bacaan Kedua Pada': status_rows[1].find_all('td')[2].text.strip(),
                  'Dibentang Oleh': bendang,
                  'Diluluskan Pada': status_rows[2].find_all('td')[2].text.strip()}

        kod_filepath, kod_filename =  file_rule.findall(kod_fileinfo)[0]

        kod_file = self._download_file(kod_filepath)
        extracted = {'kod': {'kod_name': kod_name,
                             'kod_file': {'kod_filename': kod_filename,
                                          'kod_content': kod_file}},
                     'tahun': tahun,
                     'tajuk': tajuk,
                     'status': status}
        return extracted

    def _download_file(self, filepath):
        url = TARGET_URL + filepath
        r = requests.get(url)
        if r.status_code != 200:
            # Give you none, try again next time
            return None
        # Base64 power!!!
        return base64.b64encode(r.content)
    
    def extract(self):
        # Pop those garbage
        rows = filter(lambda x: x != '\n', self.table)
        # Think if it, I don't need this
        # headrow = rows.pop(0)
        # header = map(lambda x: x.text, headrow.find_all('th'))

        # Throw out the header, use thead stupid!
        rows.pop(0)
        self.total_row = len(rows)
        print 'Yet another %s rows!' % self.total_row
        data = map(self._extract_row, rows)
        print 'Habis!'
        return data

    def extract_to_json(self):
        data = {'bill_list': self.extract()}
        return json.dumps(data)
    
if __name__ == '__main__':
    if len(sys.argv) > 2:
        sys.exit('Usage: python gov.py [HTMLFILE]')

    if len(sys.argv) == 1:
        doReq()
    elif len(sys.argv) == 2:
        htmlfile = sys.argv[1]
        html = open(htmlfile, 'rb').read()
        mytable = MyTable(html)
        # Good for the eyes
        print mytable.extract_to_json()

