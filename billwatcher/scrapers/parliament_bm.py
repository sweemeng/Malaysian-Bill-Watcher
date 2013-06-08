import requests
from xml.etree import ElementTree


class BillsLoader(object):
    def __init__(self):
        self.url = "http://www.parlimen.gov.my/bills-dewan-rakyat.html?&uweb=dr&lang=bm&arkib=yes&ajx=1"
        self.raws = requests.get(self.url)
        self.bills = []
    
    def process(self):
        root = ElementTree.fromstring(self.raws.content)
        for item in root.getchildren():
            self.bills.append(BillsData(item))



class BillsData(object):
    def __init__(self, item):
        self.field = ["name", "code", "first_read", "second_read", "presenter", "approved", "approved_by"]
        self.url = None
        self.name = item.attrib["text"]
        key = 0
        for detail in item:
            if "text" in detail.attrib:
                setattr(self, self.field[key], detail.attrib["text"])
            if detail.getchildren():
                js_str = detail.getchildren()[0].text
                self.url = js_str.split("'")[1]
            key += 1

    def show(self):
        for key in self.field:
            print "%s : %s" % (key, getattr(self,key,None))
        print "url:", self.url


                
if __name__ == "__main__":
    loader = BillsLoader()
    loader.process()
    for bill in loader.bills:
        print bill.show()
