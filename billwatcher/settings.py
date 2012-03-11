try:
    from settings_local import *
except:
    pass

PORT = 8080
HOST = "localhost"

DB_CONNECT = "sqlite:///data.db"

URL = 'http://localhost:8080/'

ITEM_PER_PAGE = 5
