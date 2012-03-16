PORT = 8080
HOST = "localhost"

DB_CONNECT = "sqlite:///data.db"

URL = 'http://localhost:8080/'

ITEM_PER_PAGE = 5

# this is to override the variable from above
try:
    from settings_local import *
except:
    pass

