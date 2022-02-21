from calendar import c
from operator import not_
from sqlite3 import Cursor
from sqlalchemy import insert, select, delete, update, and_, or_, not_
from db import Base, engine, execute
from models import User, Address

Base.metadata.create_all(engine)

#_and - &
#_or - |
#_not - ~
#a and b and c ### (a and b and c) or (not d)
#_and(a, b, c)

def insert_one_user():
    query = insert(User).values(
        name = 'John',
        fullname = 'John Carter' 
    )
    execute(query, data)

data = [
    {"name": "Alex", "fullname": "Alex Sidorov"},
    {"name": "Anna", "fullname": "Anna Karenina"},
]
def insert_many_users():
    query = insert(User)
    execute(query, data)

def select_users():
    query = (
        select(User.name, User.id) ### фильтрация столбцов
            .where(
                ~User.id.between(1, 2) |
                (User.fullname.like('j%') & User.id == 1)
            )
            #.order_by(User.id.desc())
### .where(User.name.like('A%'))
### .where(User.id.between(1, 2))
### .where(User.name.in_(['Alex', 'John', 'Gleb']))
        )
    
    with engine.connect() as conn:
        cursor = conn.execute(query)
        users = list(cursor)
    for user in users:
        print(dict(user))

select_users()

def delete_duplicate_address():
    query = delete(Address).where(Address.id == 2)
    execute(query)

def delete_duplicate_address():
    
    with engine.begin() as conn:
        query = delete(Address).where(Address.id == 1)
        conn.execute(query)
        sp = conn.begin_nested()
        query = delete(Address).where(Address.id == 3)
        conn.execute(query)
        sp.rollback(query)
        

delete_duplicate_address()

#def update_address():
   # query = (
       # update(Address)
           # .where(Address.id == 3)
           # .values(email_address = 'alex@barsun')
  #  )
    #execute(query)


update_address()