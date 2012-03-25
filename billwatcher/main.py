from bottle import run
from pages import detail
from pages import list_all
from pages import about_us
from pages import search
from pages import feed
from json_api import single_item
from json_api import all_item
from static_views import css_views,js_views
from settings import HOST,PORT
from models import initdb

initdb()
run(host=HOST,port=PORT)

