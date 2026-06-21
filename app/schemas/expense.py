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

class ExpenseUpdate(ExpenseBase):
    pass

class ExpensePatch(BaseModel):
    title: str | None = None
    amount: Decimal | None = None
    description: str | None = None
    expense_date: date | None = None
    category_id: int | None = None

class ExpenseResponseTotal(BaseModel):
    expense_date: date
    total: float
    model_config = ConfigDict(from_attributes=True)

class ExpenseCategoryTotal(BaseModel):
    id: int
    title: str
    total: float
    model_config = ConfigDict(from_attributes=True)