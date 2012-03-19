import urllib2
import urllib
import json
import os

def download(url):
    curdir = os.curdir
    file_path = os.path.join(curdir,'files') 
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    
    try:
        file_name = url.split('/')[-1]
        clean_url = urllib.quote(url.split('//')[1])
        url = 'http://%s' % clean_url
        data = urllib2.urlopen(url)
        full_path = os.path.join(file_path,file_name)
        f = open(full_path,'wb')
        f.write(data.read())
        f.close()
        return full_path
    except urllib2.HTTPError,e:
        return None
        
