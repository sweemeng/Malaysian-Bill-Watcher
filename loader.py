from BeautifulSoup import BeautifulSoup
import urllib2
from sqlalchemy import select
from sqlalchemy.sql import and_,or_
import datetime
import re
from pages import detail

from models import bills,bill_revs
from models import engine
import settings


class Bill(object):
    pass
    
    
def load_page():
    page = urllib2.urlopen('http://www.parlimen.gov.my/index.php?modload=document&uweb=dr&doc=bills&lang=en#')
    soup = BeautifulSoup(page)
    table = soup.find('table',{'id':'mytable'})
    tr = table.find('tr')
    key = ['name','year','long_name','status']
    siblings = tr.findNextSiblings('tr')
    for i in siblings:
        td = i.findAll('td')
        text = [t.text for t in td[:3]]
        result = zip(key[:3],text)
        a_link = td[0].find('a')
        t_url = a_link['onclick']
        t_url = t_url.split('(')[1]
        url = t_url.split(',')[0].replace('\'','')
        result.append(('url',url))
        status = td[3].find('div',{'class':'parent'})
        if status:
            result.append((key[3],status.text))
            in_table = td[3].find('table')
            translation = {
                'Dibentang Oleh':'read_by',
                'Disokong Oleh':'supported_by',
                'Dibentang Pada':'date_presented'
                }
            for j in in_table.findAll('tr'):
                i_td = j.findAll('td')
                tpl = (translation[i_td[0].text],i_td[2].text)
                result.append(tpl)
        else:
            t = td[3].text.splitlines()
            result.append((key[3],t[0]))
        b = Bill()
        tmp = [setattr(b,r[0],r[1]) for r in result]
        yield b
            
    
def load_data():
    print 'loading'
    pg = load_page()
    conn = engine.connect()
    print 'here we go'
    for i in pg:
        message = ''
        check = select([bills.c.id],bills.c.name == i.name)
        result = conn.execute(check)
        res = result.fetchone()
        if not res:
            bill = bills.insert().values(name=i.name,long_name=i.long_name)
            result = conn.execute(bill)
            pkey = result.inserted_primary_key[0]
        else:
            pkey = res['id']
        
        # We check existing bills, remember we save link for bother the bills and revision
        check = select([bill_revs],and_(
            bill_revs.c.bill_id == int(pkey),
            bill_revs.c.year == int(i.year)))
  

        key = [k for k in dir(i) if not re.match('^__',k)]
        val = [getattr(i,k) for k in key]
        data = dict(zip(key,val))
        data['bill_id'] = pkey
        
        if 'date_presented' in key:
            data['date_presented'] = datetime.datetime.strptime(i.date_presented,'%d/%m/%Y').date()

        result = conn.execute(check)
        bill_rev = result.fetchone()
        exec_insert = False

        if not bill_rev:
            data['create_date'] = datetime.datetime.now()
            data['update_date'] = datetime.datetime.now()
            revision = bill_revs.insert().values(**data)
            message = 'Bills Started: %s, year %s %s'
            exec_insert = True
        else:
            data['update_date'] = datetime.datetime.now()
            # because the bills is always under debate. so for the same year, and the status change, 
            if bill_rev['status'] != i.status:
                revision = bill_revs.update().\
                    where(
                        and_(
                            bill_revs.c.bill_id == int(pkey),
                            bill_revs.c.year == int(i.year)
                            )
                        ).\
                    values(**data)
                message = 'Bills Updated: %s, year %s %s'
                exec_insert = True
        if exec_insert:
            result = conn.execute(revision)
        url = settings.URL + '/detail/%d/' % (pkey)
        if message:
            print message % (i.long_name, i.year,URL+url)


if __name__ == '__main__':
    load_data()
