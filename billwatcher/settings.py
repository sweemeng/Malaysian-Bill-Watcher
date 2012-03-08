URL = 'http://localhost:8080/'
ITEM_PER_PAGE = 5

DB_CONNECT = "sqlite:///data.db"

PORT = 8080
HOST = "localhost"

try:
    from settings_local import *
except:
    pass
