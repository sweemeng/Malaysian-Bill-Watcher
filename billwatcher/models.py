from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import relationship

from sqlalchemy import func
from sqlalchemy import Column
from sqlalchemy import Integer, String, ForeignKey, Date, DateTime
from sqlalchemy import create_engine

from settings import DB_CONNECT

maker = sessionmaker()

DBSession = scoped_session(maker)

Base = declarative_base()

def initdb():
    engine = create_engine(DB_CONNECT)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

class Bill(Base):
    __tablename__ = 'bills'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    long_name = Column(String)

class BillRevision(Base):
    __tablename__ = 'bill_revs'

    id = Column(Integer, autoincrement=True, primary_key=True)
    url = Column(String)
    status = Column(String)
    year = Column(String)
    read_by = Column(String)
    supported_by = Column(String)
    date_presented = Column(Date)
    bill_id = Column(Integer, ForeignKey('bills.id',
                                         onupdate='CASCADE',
                                         ondelete='CASCADE'))
    # This creates a server side default
    created_date = Column(DateTime, server_default=func.now())
    # Example,
    # This creates a runtime default, more flexible
    # import datetime
    # create_date = Column(Date, default=datetime.datetime.now)
    update_date = Column(DateTime)

    # This will make relationship accessible
    # You can access Bill object now via calling cls.bill
    # uselist means it's many to one relationship to bill
    # backref declares linkback so you can get all related revisions from bill
    # via cls.bill_revs
    # There's a lot of to read on this
    bill = relationship('Bill', uselist=False, backref='bill_revs')

initdb()
