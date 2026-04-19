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


def add_db(user,text,email,card_number,card_expiry):#working
    password = generate_password_hash(text,method="pbkdf2:sha256")
    person = User(name=user,text=password,email=email,card_number=card_number,card_expiry=card_expiry)
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

def updatedb(name,text,id,email,card_number,card_expiry):#work
    try:
        values = {}
        if name:
            values["name"] = name
        if text:
            values["text"] = text
        if email:
            values["email"] = email
        if card_number:
            values["card_number"] = card_number
        if card_expiry:
            values["card_expiry"] = card_expiry
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
def autoriz_check(name,password1):
    with Session() as session:
            user = session.query(User).where(User.name == name).first()
            if user and check_password_hash(user.password, password1):
                return True
            else:
                return False