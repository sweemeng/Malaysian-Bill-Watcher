import bottle
import settings
import models
from pages import detail
from pages import list_all
from pages import about_us
from pages import search
from pages import feed
from json_api import single_item
from json_api import all_item
from static_views import css_views
from static_views import js_views

models.initdb()
bottle.run(server='gunicorn',host=settings.HOST,port=settings.PORT)
