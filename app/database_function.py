import os
import sqlalchemy as db
from app.classes import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import delete, update
from werkzeug.security import generate_password_hash, check_password_hash

basedir = os.path.abspath(os.path.dirname(__file__))
db_path= os.path.join(basedir, "Users.db")
engine = db.create_engine(f"sqlite:///{db_path}")
Session = sessionmaker(bind=engine)
Base = declarative_base()
Base.metadata.create_all(engine)


def add_db(user,text):#working
    password = generate_password_hash(text,method="pbkdf2:sha256")
    person = User(name=user,text=password)
    with Session() as session:
        if session.query(User.id).filter_by(name = user).first() is not None:
            return False
        else:
            session.add(person)
            session.commit()
            return True
def delete_db(id):#50/50
    with Session() as session:
        if session.query(User.id).filter_by(id=id).first():

            stm= delete(User).where(User.id == id)
            session.execute(stm)
            session.commit()
            return True
        else:
            return False
def read1_db(id):# working!
    with Session() as session:
        find = session.query(User).where(User.id == id).first()
        if find:
            return find
        else:
            return "Error"
def readall():#working
    try:
        with Session() as session:
            all_data = session.query(User.id,User.name).all()
            return all_data
    except:
        return None
def readlast():#work
    with Session() as session:
        try:
            last_data = session.query(User.id,User.name).order_by(User.id.desc()).first()
            if last_data is not None:
                return last_data
            else:
                return None
        except:
            return None

def updatedb(name,text,id):#work
    try:
        values = {}
        if name:
            values["name"] = name
        if text:
            values["text"] = text
        if not values:
            return False
        if id and id > 0:
            with Session() as session:
                up = update(User).where(User.id == id).values(**values)
                session.execute(up)
                session.commit()
            return True
    except:
            return False
def autoriz_check(name,password):
    with Session() as session:
            a = check_password_hash(user.text, password)
            print (a)
            user = session.query(User).where(User.name == name).first()
            if user and check_password_hash(user.text, password):
                return True
            else:
                return False