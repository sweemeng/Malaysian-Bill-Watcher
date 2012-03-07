# deprecated
class Bill(object):
    pass

# webhelpers package has it :)
class Pagination(object):
    def __init__(self, item_per_page, total_item, page_no=None):
        if page_no:
            self.page_no = int(page_no)
        else:
            self.page_no = 1
        self.item_per_page = item_per_page
        self.first = (self.page_no - 1)  *  self.item_per_page 
        self.last = self.page_no * self.item_per_page
        self.total_item = total_item
        self.page_list = range(self.total_item/self.item_per_page)
        self.page_list = [i+1 for i in self.page_list]
        self.next_page = self.page_no + 1
        self.prev_page = self.page_no - 1

def get_keys(keys):
    split_keys = keys.split('_')
    if 'revs' in split_keys:
        keys = '_'.join(split_keys[2:])
    else:
        keys = '_'.join(split_keys[1:])
    return keys

# deprecated
def get_bill(row):
    bill = Bill()
    for key in row.keys()[1:]:
        if key != 'bills_id':
            new_key = get_keys(key)
            setattr(bill,new_key,row[key])
    return bill


