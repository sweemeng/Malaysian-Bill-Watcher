class Bill(object):
    pass


class Pagination(object):
    def __init__(self,item_per_page,total_item,page_no=None):

        if page_no:
            self.page_no = int(page_no)
        else:
            self.page_no = 1
        self.extra_page = 0
        self.item_per_page = item_per_page
        self.total_item = total_item
        self.extra_item = self.total_item % self.item_per_page
        if self.extra_item:
            self.extra_page = 1 
        self.total_page = (self.total_item / self.item_per_page) + self.extra_page
        self.page_list = range(self.total_page)
        self.page_list = [i+1 for i in self.page_list]
        self.next_page = self.page_no + 1
        self.prev_page = self.page_no - 1
        self.first = (self.page_no - 1)  *  self.item_per_page 
        if self.page_no == self.page_list[-1] and self.extra_item:
            self.last = self.total_item
        else:
            self.last = self.page_no * self.item_per_page

             


def get_keys(keys):
    split_keys = keys.split('_')
    if 'revs' in split_keys:
        keys = '_'.join(split_keys[2:])
    else:
        keys = '_'.join(split_keys[1:])
    return keys

def get_bill(row):
    bill = Bill()
    for key in row.keys()[1:]:
        if key != 'bills_id':
            new_key = get_keys(key)
            setattr(bill,new_key,row[key])
    return bill


