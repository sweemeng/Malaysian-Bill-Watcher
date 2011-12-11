from bottle import run
from pages import detail
from pages import list_all
from pages import server_css

run(server='gunicorn')

