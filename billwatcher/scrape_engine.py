from BeautifulSoup import BeautifulSoup
import urllib2


class TableExtractor(object):
    def __init__(self,url):
        self.url = url
        page = urllib2.urlopen(self.url)
        self.soup = BeautifulSoup(page)

    def extract_table(self,root,table_id):
        tables = root.findAll('table',
                {'id':table_id})
        return tables

    def extract_rows(self,table):
        rows = table.findAll('tr')
        return rows

    def extract_columns(self,rows):
        columns = rows.findAll('td')
        return [i for i in columns]

    def extract_data(self,columns,with_links=False,links_only=False):
        output = []
        if with_links:
            links = columns.findAll('a')
            if links:
                for link in links:
                    if link.get('href') and link.get('href') != '#':
                        output.append(link.get('href'))
                    elif link.get('onclick'):
                        url = link.get('onclick')
                        url = url.split('(')[1]
                        url = url.split(',')[0].replace("'", '')
                        output.append(url)
                    if not links_only:
                        output.append(link.text)
                return output
        else:
            output.append(columns.text)
        return output

    def run(self):
        tables = self.extract_table(self.soup,'mytable')
        for table in tables:
            rows = self.extract_rows(table)
            for row in rows:
                column = self.extract_columns(row)
                yield [ self.extract_data(i,with_links=True) for i in column ]


