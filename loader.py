from BeautifulSoup import BeautifulSoup
import urllib2


class Bill(object):
    pass
    
    
def load_page():
    page = urllib2.urlopen('http://www.parlimen.gov.my/index.php?modload=document&uweb=dr&doc=bills')
    soup = BeautifulSoup(page)
    table = soup.find('table',{'id':'mytable'})
    tr = table.find('tr')
    key = [k.text for k in tr.findAll('th')]
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
            for j in in_table.findAll('tr'):
                i_td = j.findAll('td')
                tpl = (i_td[0].text,i_td[2].text)
                result.append(tpl)
        else:
            t = td[3].text.splitlines()
            result.append((key[3],t[0]))
        b = Bill()
        tmp = [setattr(b,r[0],r[1]) for r in result]
        yield b
            
    
