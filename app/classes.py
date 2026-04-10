from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__='user'

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(unique=True)
    password:Mapped[str] = mapped_column(String(255), nullable=False)
    email:Mapped[str] = mapped_column(unique=True)
    card_number:Mapped[str | None] = mapped_column(String(20))
    card_expiry: Mapped[str | None] = mapped_column(String(5))
    def __repr__(self):
        return f"{self.id}:{self.name}->{self.text}"
