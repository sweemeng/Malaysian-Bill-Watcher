from bottle import route,request
from models import engine,bills,bill_revs
from sqlalchemy import select
import datetime

@route('/api/single/',method='GET')
def single_item():
    id = request.GET.get('id')
    return get_item(id)

@route('/api/all/',method='GET')
def all_item():
    id_query = select([bills.c.id])
    conn = engine.connect()
    result = conn.execute(id_query)
    data = []
    
    ids = result.fetchall()
    for i in ids:
        data.append(get_item(i['id']))
    return {'data':data}
    
def get_item(id):
    bill_query = select([bills],bills.c.id==id)
    
    data = {}
    conn = engine.connect()
    result = conn.execute(bill_query)
    
    bill = result.fetchone()
    
    for i in bill.keys():
        data[i] = bill[i]
    
    rev_query = select([bill_revs],bill_revs.c.bill_id==id)
    result = conn.execute(rev_query)
    
    revision = result.fetchall()
    data['revision'] = []
    
    for rev in revision:
        temp = {}
        for key in rev.keys():
            if type(rev[key]) == datetime.datetime:
                temp[key] = rev[key].strftime('%d/%m/%Y %H:%M:%s')
            elif type(rev[key]) == datetime.date:
                temp[key] = rev[key].strftime('%d/%m/%Y') 
            else:
                temp[key] = rev[key]

        data['revision'].append(temp) 
    
    return data

