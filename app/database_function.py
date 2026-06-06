from sqlalchemy import delete, update, select
from werkzeug.security import generate_password_hash, check_password_hash
from app.create_db import engine, Session, Base
from app.classes import User , Ticket
from flask_login import current_user



Base.metadata.create_all(engine)
session = Session
def add_db(user,text,email):#working
    password = generate_password_hash(text,method="pbkdf2:sha256")
    person = User(name=user,password=password,email=email)
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
def read1_db_email(email):# working!
    with Session() as session:
        find = session.query(User).where(User.email == email).first()
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

def updatedb(name,text,id,email,card_number,card_expiry):
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
            user = session.query(User).where(User.email == name).first()
            if user and check_password_hash(user.password, password1):
                return True
            else:
                return False
def ticket_add_db(place,uniqe_id):#working
    person_ticket = Ticket(user_id = current_user.id ,place = place, uniqe_id=uniqe_id)
    with Session() as session:
        if session.query(Ticket.ticket_id).filter_by(uniqe_id = uniqe_id).first() is not None:
            return False
        else:
            session.add(person_ticket)
            session.commit()
            return True
def ticket_delete_db(id):#50/50
    with Session() as session:
        if session.query(Ticket.ticket_id).filter_by(ticket_id=id).first():

            delete_ticket= delete(Ticket).where(Ticket.ticket_id == id)
            session.execute(delete_ticket)
            session.commit()
            return True
        else:
            return False
def ticket_read1_db(id):# working!
    with Session() as session:
        find_ticket = session.query(Ticket).where(Ticket.user_id == id).first()
        if find_ticket:
            return find_ticket
        else:
            return "Error"
def ticket_readall():#working
    try:
        with Session() as session:
            ticket_all_data = session.query((Ticket.ticket_id,Ticket.owner,Ticket.uniqe_id,Ticket.place,Ticket.user_id)).all()
            return ticket_all_data
    except:
        return None
def ticket_readlast():#work
    with Session() as session:
        try:
            last_data_ticket = session.query(Ticket.ticket_id,Ticket.owner,Ticket.uniqe_id,Ticket.place,Ticket.user_id).order_by(Ticket.ticket_id.desc()).first()
            if last_data_ticket is not None:
                return last_data_ticket
            else:
                return None
        except:
            return None

def ticket_updatedb(place,uniqe_id):
    try:
        values = {}
        if place:
            values["place"] = place
        if uniqe_id:
            values["uniqe_id"] = uniqe_id
        if not values:
            return False
        if uniqe_id and uniqe_id > 0:
            with Session() as session:
                up = update(Ticket).where(Ticket.uniqe_id == id).values(**values)
                session.execute(up)
                session.commit()
            return True
    except:
            return False
def get_user_tickets(user_id):
    with Session() as session:
        stmt = select(Ticket).where(Ticket.user_id == user_id)

        return session.execute(stmt).scalars().all()