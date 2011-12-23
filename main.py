from bottle import run
from pages import detail
from pages import list_all
from json_api import single_item
from json_api import all_item
from pages import converted_pdf_view

run(host='localhost',port=8080)

