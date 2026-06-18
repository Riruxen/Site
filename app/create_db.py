import os
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "Users.db")

engine = db.create_engine(f"sqlite:///{db_path}")
@event.listens_for(Engine,'connect')
def set_sqlite_pragma(dbapi_connection, connection_record):
    cur = dbapi_connection.cursor()
    cur.execute('PRAGMA foreign_keys=ON')
    cur.close()
Session = sessionmaker(bind=engine)
Base = declarative_base()