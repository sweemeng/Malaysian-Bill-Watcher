# webhelpers package has it :)
class Pagination(object):
    def __init__(self,item_per_page,pages_displayed,total_item,page_no=None):
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

        half_page = pages_displayed / 2
        start_active = self.page_no - half_page
        end_active = self.page_no + half_page
        last_pages = total_item - pages_displayed

        if self.page_no in self.page_list[:pages_displayed]:
            if start_active <= 1:
                self.active_list = self.page_list[:pages_displayed]
            else:
                self.active_list = self.page_list[start_active:end_active]
        elif self.page_no in self.page_list[last_pages:]:
            if end_active >= len(self.page_list):
                self.active_list = self.page_list[last_pages:]
            else:
                self.active_list = self.page_list[start_active:end_active]

        else:
            self.active_list = self.page_list[start_active:end_active]


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


