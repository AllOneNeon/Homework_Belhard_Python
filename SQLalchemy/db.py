from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

#SQLite
url = 'sqlite:///local.db'

#Postgres
#user = 'postgres'
#passwd = 'postgres'
#host = 'localhost'
#port = 5432
#db = 'postgres'
#yrl = f'postgresql://{user}:{passwd}@{host}:{port}/{db}'

engine = create_engine(url, echo=True)
Base = declarative_base()

def execute(*args, **kwargs):
    with engine.connect() as conn:
        return conn.execute(*args, **kwargs)