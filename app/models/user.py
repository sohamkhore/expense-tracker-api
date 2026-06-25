from app.database import Base
from sqlalchemy import Integer, String, Column, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index= True)
    username = Column(String,unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default= datetime.utcnow ,nullable=False)
    expenses = relationship(
        "Expense",
        back_populates="user"
    )
    categories = relationship(
    "Category",
    back_populates="user"
    )
