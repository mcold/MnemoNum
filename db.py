# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

db_name = os.getcwd() + '\MnemoNum.db'
Base = declarative_base()
#engine = create_engine('sqlite:///' + db_name)
engine = create_engine('sqlite:///MnemoNum.db')
Session = sessionmaker(bind=engine)
session = Session()


class Mnemo(Base):
    __tablename__ = 'mnemos'

    num = Column(Integer, primary_key=True)
    mnemo = Column(String(100))


class Month(Base):
    __tablename__ = 'months'

    num = Column(Integer, primary_key=True)
    month = Column(String(100))

class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    tag = Column(String(300))


def create_db():
    Base.metadata.create_all(engine)

def add_tag(tag):
    ins_tag(tag)
    l = select_tags()
    return l

def select_tags():
    l = []
    for row in session.query(Tag).all():
        x = row.tag
        l.append(x)
    return l


def ins_tag(tag):
    t = Tag(tag = tag.decode('utf-8'))
    session.add(t)
    session.commit()



def populate_data():
    # mnemos
    for i in range(0, 1000):
        mnem = Mnemo(num=i)
        session.add(mnem)
    session.commit()

    # months
    for i in range(1, 13):
        month = Month(num=i)
        session.add(month)
    session.commit()


def populate_month():
    # months
    for i in range(1, 13):
        month = Month(num=i)
        session.add(month)
    session.commit()

def initialize_db():
    if not os.path.exists(db_name):
        create_db()
        populate_data()


def select_months():
    """
        Select months from db
    :return:
    """
    l = []
    for row in session.query(Month).all():
        #print(row.month)
        x = row.month
        l.append(x)
    return l




def select_mnemo(mnemo=None):
    """
        Select data from db
    :return: dictionary [num] = mnemo
    """
    d = {}

    if mnemo==None:
        for row in session.query(Mnemo).all():
            d[row.num] = row.mnemo
    else:
        # if digit
        if mnemo.isdigit():
            for row in session.query(Mnemo).filter(Mnemo.num.like(u'%{0}%'.format(mnemo.decode('utf-8')))).all():
                d[row.num] = row.mnemo
        else:
            for row in session.query(Mnemo).filter(Mnemo.mnemo.like(u'%{0}%'.format(mnemo.decode('utf-8')))).all():
                d[row.num] = row.mnemo
    return d

def select_tag_like(text=None):
    """
        Select data from db
        :return: list dates
    """
    l = []

    if text==None:
        for row in session.query(Tag).all():
            l.append(row.tag)
    else:
        for row in session.query(Tag).filter(Tag.tag.like(u'%{0}%'.format(text.decode('utf-8')))).all():
            l.append(row.tag)

    return l

def select_mnemo_by_num(num=None):
    """
        Select data from db
    :return: dictionary [num] = mnemo
    """

    d = {}
    if num==None:
        for row in session.query(Mnemo).all():
            d[row.num] = row.mnemo
    else:
        for row in session.query(Mnemo).filter(Mnemo.num.like(u'%{0}%'.format(num.decode('utf-8')))).all():
            d[row.num] = row.mnemo
    return d


def select_mnemo_for_test():
    d = {}
    for row in session.query(Mnemo).all():
        if not row.mnemo in (None, ''):
            d[row.num] = row.mnemo
    return d

def update_mnemo(num, mnem):
    num = str(num)
    mnem = mnem.decode('utf-8')
    num = num.decode('utf-8')
    session.query(Mnemo).filter(Mnemo.num == num). \
        update({Mnemo.mnemo: mnem}, synchronize_session='evaluate')
    session.commit()

def update_month(num, mnem):
    num = str(num)
    mnem = str(mnem)
    num = num.decode('utf-8')
    mnem = mnem.decode('utf-8')

    session.query(Month).filter(Month.num == num). \
        update({Month.month: mnem}, synchronize_session='evaluate')
    session.commit()

def select_mnemo_for_label(num):
    num = str(num)
    #num = num.decode('utf-8')
    for row in session.query(Mnemo).filter(Mnemo.num == num).all():
        return row.mnemo


if __name__ == '__main__':
    create_db()
    populate_month()
