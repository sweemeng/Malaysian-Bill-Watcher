PORT = 8080
HOST = "localhost"

DB_CONNECT = "sqlite:///data.db"

URL = 'http://billwatcher,sinarproject.org/'

ITEM_PER_PAGE = 5
PAGE_DISPLAYED = 10

# this is to override the variable from above
try:
    from settings_local import *
except:
    pass

