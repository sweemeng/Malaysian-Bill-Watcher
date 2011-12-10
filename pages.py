from bottle import route,view,static_file
from models import bills,bill_revs
from models import engine
from sqlalchemy import select

@route('/detail/<id>/')
@view('detail')
def detail(id):
    bl = select([bills],bills.c.id == id)
    conn = engine.connect()
    
    result = conn.execute(bl)
    bill = result.fetchone()
    rev = select([bill_revs],bill_revs.c.bill_id == bill['id']).\
        order_by(bill_revs.c.year.desc())
    
    result = conn.execute(rev)
    revision = result.fetchall()
    return dict(bill=bill,revision=revision)

@route('/<page_no>/')
@view('list')
def list_all(page_no):
    
    first = (page_no - 1)  *  5 + 1
    last = 5 * page_no
    bl = select([bills,bill_revs],and_(
        bills.c.id==bill_revs.c.bill_id,
        bills.c.id>=first,bills.c.id<=last
        )
    )
    conn = engine.connect()
    result = conn.execute(bl)
    bill = result.fetchall()
    
    return dict(bill=bill)
    
@route('/css/<filename>')
def server_css(filename):
    return static_file(filename,root='./css/')
