import logging
import urllib2
import datetime

from BeautifulSoup import BeautifulSoup

import models
import settings

log = logging.getLogger(__name__)

class Bill(object):
    def __init__(self, **kw):
        for k, v in kw.iteritems():
            setattr(self, k, v)

def load_page():
    page = urllib2.urlopen('http://www.parlimen.gov.my/index.php?modload=document&uweb=dr&doc=bills&lang=en#')
    soup = BeautifulSoup(page)
    table = soup.find('table', {'id':'mytable'})
    tr = table.find('tr')
    key = ['name', 'year', 'long_name', 'status']
    translation = {'Dibentang Oleh':'read_by',
                   'Disokong Oleh':'supported_by',
                   'Dibentang Pada':'date_presented'}
    siblings = tr.findNextSiblings('tr')
    for i in siblings:
        td = i.findAll('td')
        text = [t.text for t in td[:3]]
        result = dict(zip(key[:3], text))
        a_link = td[0].find('a')
        t_url = a_link['onclick']
        t_url = t_url.split('(')[1]
        url = t_url.split(',')[0].replace("'", '')
        result['url'] = url
        status = td[3].find('div', {'class':'parent'})
        if status:
            result[key[3]] = status.text
            in_table = td[3].find('table')
            s_tr = in_table.findAll('tr')
            for j in s_tr:
                i_td = j.findAll('td')
                result[translation[i_td[0].text]] = i_td[2].text
        else:
            t = td[3].text.splitlines()
            result[key[3]] = t[0]
        # yield Bill(**result)
        yield result

def load_data():
    print 'Loading...'
    bills = load_page()
    print 'Here we go'

    session = models.DBSession()
    for b in bills:
        message = ''
        bill = (session.query(models.Bill)
                .filter(models.Bill.name==b['name'])
                .first())

        if not bill:
            bill = models.Bill(name=b['name'],
                               long_name=b['long_name'])
            session.add(bill)
            session.flush()

        b['bill_id'] = bill.id

        if b.has_key('date_presented'):
            b['date_presented'] = datetime.datetime.strptime(b['date_presented'],
                                                             '%d/%m/%Y').date()

        rev = (session.query(models.BillRevision)
               .filter(models.BillRevision.bill_id==bill.id)
               .filter(models.BillRevision.year==int(b['year']))
               .first())

        now = datetime.datetime.now()
        b['update_date'] = now
        if not rev:
            b['create_date'] = now
            rev = models.BillRevision(**b)
            session.add(rev)
            session.flush()
            message = 'Bill Started: %s, year %s %s'
        else:
            if rev.status != b['status']:
                for k, v in b.iteritems():
                    if hasattr(rev, k):
                        setattr(rev, k, v)
                session.flush()
                message = 'Bills Updated: %s, year %s %s'

        if message:
            url = settings.URL + 'detail/%d/' % (bill.id)
            print message % (bill.long_name, rev.year, url)
    session.commit()

if __name__ == '__main__':
    models.initdb()
    load_data()
