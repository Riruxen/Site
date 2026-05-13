import os
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "Users.db")

engine = db.create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)
Base = declarative_base()