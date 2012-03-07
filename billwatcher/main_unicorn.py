import bottle
import settings
import log
import models
from pages import detail
from pages import list_all
from pages import about_us
from pages import search
from pages import feed
from json_api import single_item
from json_api import all_item

log.initlog()
models.initdb()
bottle.debug(True)
bottle.run(server='gunicorn', port=settings.PORT)

