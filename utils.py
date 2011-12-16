class Bill(object):
    pass

def get_keys(keys):
    split_keys = keys.split('_')
    if 'revs' in split_keys:
        keys = '_'.join(split_keys[2:])
    else:
        keys = '_'.join(split_keys[1:])
    return keys

def get_bil(row):
    bill = Bill()
    for key in row.keys():
        if key != 'bills_id':
            new_key = get_keys(key)
            setattr(bill,new_key,row[key]
    return bill
