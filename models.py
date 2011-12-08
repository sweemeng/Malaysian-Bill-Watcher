from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer,String,ForeignKey,Date,Sequence
from sqlalchemy import MetaData
from sqlalchemy import create_engine

metadata=MetaData()
engine = create_engine('sqlite:///data.db')

bills = Table('bills',metadata,
    Column('id',Integer,Sequence('bills_id_seq'),primary_key=True),
    
    Column('name',String),
    Column('long_name',String)
    )

# bill revision
bill_revs = Table('bill_revs',metadata,
    Column('id',Integer,Sequence('bill_revs_id_seq'),primary_key=True),
    Column('url',String),
    Column('status',String),
    Column('year',Integer),
    Column('read_by',String),
    Column('supported_by',String),
    Column('date_presented',Date),
    Column('bill_id',None,ForeignKey('bills.id'))
    )
    
metadata.create_all(engine)
