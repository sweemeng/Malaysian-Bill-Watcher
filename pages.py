from bottle import route,view,static_file
from models import bills,bill_revs
from models import engine
from sqlalchemy import select

@route('/<id>/')
@view('detail')
def detail(id):
    bl = select([bills],bills.c.id == id)
    conn = engine.connect()
    
    result = conn.execute(bl)
    bill = result.fetchone()
    rev = select([bill_revs],bill_revs.c.bill_id == bill['id']).\
        order_by(bill_revs.c.year.desc())
    
    result = conn.execute(rev)
    revision = result.fetchone()
    return dict(bill=bill,revision=revision)
    
    
@route('/css/<filename>')
def server_css(filename):
    return static_file(filename,root='./css/')