from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__='user'

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(unique=True)
    password:Mapped[str]
    Email:Mapped[str] = mapped_column(unique=True)
    Kartenummer:Mapped[int]
    data:Mapped[int]
    CVV:Mapped[int]
    def __repr__(self):
        return f"{self.id}:{self.name}->{self.text}"
