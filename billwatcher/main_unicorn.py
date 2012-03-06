from bottle import run
from pages import detail
from pages import list_all
from pages import about_us
from pages import search
from pages import feed
from json_api import single_item
from json_api import all_item
from settings import PORT

run(server='gunicorn',port=PORT)

