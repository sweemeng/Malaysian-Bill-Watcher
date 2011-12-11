from bottle import run
from pages import detail
from pages import list_all
from pages import server_css
from json_api import single_item
from json_api import all_item


run(server='gunicorn')

