from bottle import route,view,static_file,request
from models import bills,bill_revs
from models import engine
from sqlalchemy import select
from sqlalchemy.sql import and_,func


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

@route('/')
@view('list')
def list_all():
    print request.GET.keys()
    if request.GET.get('page_no'):
        page_no = int(request.GET.get('page_no'))
    else:
        page_no = 1
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

    cnt = select([bills])
    result = conn.execute(cnt)
    count = result.fetchall()
   
    page_list = range(len(count) / 5)
    page_list = [i+1 for i in page_list]
    return dict(bill=bill,page_list=page_list,page_no=page_no,
        next_page=page_no+1,prev_page=page_no-1)
    
@route('/css/<filename>')
def server_css(filename):
    return static_file(filename,root='./css/')
