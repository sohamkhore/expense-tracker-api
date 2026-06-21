from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db

from app.schemas.expense import ExpenseCreate, ExpenseResponse
from app.models.expense import Expense
from app.models.category import Category

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.post("/add_expense", response_model= ExpenseResponse)
def create_expense( expense: ExpenseCreate, db: Session = Depends(get_db)):

    category_check = db.query(Category).filter(Category.id == expense.category_id).first()
    if not category_check :
        raise HTTPException(
            status_code = 400,
            detail = "Category doesnt exists"
        )

    # existing = db.query(Expense).filter(Expense.title == expense.title).first()
    # if existing:
    #     raise HTTPException(
    #         status_code = 
    #     )

    new_expense = Expense(
    title=expense.title,
    amount=expense.amount,
    description=expense.description,
    expense_date=expense.expense_date,
    category_id=expense.category_id
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


@router.get("/",response_model= list[ExpenseResponse])
def get_all_expenses(db: Session = Depends(get_db)):
    
    all_expenses = db.query(Expense).all()

    return all_expenses


@router.get("/{expense_id}", response_model= ExpenseResponse)
def get_expense_by_id( expense_id : int, db: Session = Depends(get_db)):

    existing = db.query(Expense).filter(expense_id == Expense.id).first()
    if not existing:
        raise HTTPException(
            status_code = 400,
            detail = "Expense not found"
        )
    return existing


@router.delete("/delete/{expense_id}")
def delete_expense_by_id(expense_id : int , db: Session = Depends(get_db)):

    find_expense=db.query(Expense).filter(Expense.id == expense_id).first()

    if not find_expense:
        raise HTTPException(
            status_code = 400,
            detail = "Expense doesnt exist"
        )

    db.delete(find_expense)
    db.commit()

    return {
         "message":"Expense deleted successfully"
    }

