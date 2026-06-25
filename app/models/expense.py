from app.database import Base
from sqlalchemy import Integer, ForeignKey, Column, String, NUMERIC, DATE
from sqlalchemy.orm import relationship

class Expense(Base):
    __tablename__ = "expenses"

    id= Column(Integer, primary_key=True,index = True)
    title= Column(String,index = True, nullable=False)
    amount= Column(NUMERIC,nullable=False)
    description=Column(String)
    expense_date=Column(DATE, nullable=False)
    category_id= Column(Integer,ForeignKey("categories.id"),nullable=False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    category = relationship(
        "Category",
        back_populates="expenses"
    )
    user = relationship(
        "User",
        back_populates="expenses"
    )
