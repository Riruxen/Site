from sqlalchemy import String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin 
from app.create_db import Base
class User(Base,UserMixin):
    __tablename__='user'

    id:Mapped[int] = mapped_column(primary_key=True) 
    name:Mapped[str] = mapped_column(unique=True)
    password:Mapped[str] = mapped_column(String(255), nullable=False)
    email:Mapped[str] = mapped_column(unique=True)
    buyed_tickets: Mapped[list['Ticket']]= relationship(back_populates='owner', cascade='all, delete-orphan', passive_deletes=True)
    def __repr__(self):
        return f"{self.id}:{self.name}->"

class Ticket(Base):
    __tablename__='tickets'

    ticket_id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id",ondelete="CASCADE"))
    place:Mapped[str] = mapped_column()
    uniqe_id:Mapped[int] = mapped_column(unique=True)
    owner:Mapped[User] = relationship(back_populates='buyed_tickets')
