from app.database import Base
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    expenses = relationship(
        "Expense",
        back_populates="category"
    )