from pydantic import BaseModel, ConfigDict
from datetime import date
from decimal import Decimal
from app.schemas.category import CategoryResponse

class ExpenseBase(BaseModel):
    title: str
    amount: Decimal
    description: str | None = None
    expense_date: date
    category_id: int

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: Decimal
    description: str | None = None
    expense_date: date
    category: CategoryResponse
    model_config = ConfigDict(from_attributes=True)