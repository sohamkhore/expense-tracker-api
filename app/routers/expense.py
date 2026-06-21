from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from sqlalchemy import func

from app.schemas.expense import ExpenseCreate, ExpenseResponse, ExpenseUpdate, ExpensePatch, ExpenseResponseTotal, ExpenseCategoryTotal
from app.models.expense import Expense
from datetime import date
from app.models.category import Category

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

##------------------------------------------------------------------------------------------------------##
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
##------------------------------------------------------------------------------------------------------##


@router.get("/",response_model= list[ExpenseResponse])
def get_all_expenses(db: Session = Depends(get_db)):
    
    all_expenses = db.query(Expense).all()

    return all_expenses
##------------------------------------------------------------------------------------------------------##


@router.get("/{expense_id}", response_model= ExpenseResponse)
def get_expense_by_id( expense_id : int, db: Session = Depends(get_db)):

    existing = db.query(Expense).filter(expense_id == Expense.id).first()
    if not existing:
        raise HTTPException(
            status_code = 400,
            detail = "Expense not found"
        )
    return existing
##------------------------------------------------------------------------------------------------------##


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
##------------------------------------------------------------------------------------------------------##


@router.put("/update_record/{expense_id}", response_model= ExpenseResponse)
def update_expense_full(updated_expense : ExpenseUpdate, expense_id: int, db: Session = Depends(get_db)):

    category_exists = (db.query(Category).filter(Category.id == updated_expense.category_id).first())
    expense_record = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense_record:
        raise HTTPException(status_code=404, detail="Expense not found")

    if not category_exists:
        raise HTTPException(
            status_code = 400,
            detail = "Category not found"
        )
    
    expense_record.title = updated_expense.title
    expense_record.amount = updated_expense.amount
    expense_record.description = updated_expense.description
    expense_record.expense_date = updated_expense.expense_date
    expense_record.category_id = updated_expense.category_id

    
    db.commit()
    db.refresh(expense_record)

    return expense_record
##------------------------------------------------------------------------------------------------------##


@router.patch("/update_record_something/{expense_id}", response_model=ExpenseResponse)
def update_expense_something(update_expense: ExpensePatch, expense_id: int, db: Session = Depends(get_db)):

    expense_exists = (db.query(Expense).filter(Expense.id == expense_id).first())
    if not expense_exists:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    update_data = update_expense.model_dump(exclude_unset=True)

    # Validate category only if user is updating category_id
    if "category_id" in update_data:
        category_exists = (
            db.query(Category).filter(Category.id == update_data["category_id"]).first())

        if not category_exists:
            raise HTTPException(
                status_code=400,
                detail="Provided Category ID does not exist"
            )

    # Update only provided fields
    for key, value in update_data.items():
        setattr(expense_exists, key, value)

    db.commit()
    db.refresh(expense_exists)

    return expense_exists
##------------------------------------------------------------------------------------------------------##


@router.get("/get_expense_by_category/{category_id}",response_model= list[ExpenseResponse])
def get_expense_by_category(category_id : int, db: Session = Depends(get_db)):

    category_exists = db.query(Category).filter(Category.id == category_id).first()
    if not category_exists :
        raise HTTPException(
            status_code = 400,
            detail = "Category not found"
        )
    
    all_expenses = db.query(Expense).filter(Expense.category_id == category_id).all()

    return all_expenses
##------------------------------------------------------------------------------------------------------##


@router.get("/expense_by_date/{date}", response_model=list[ExpenseResponse])
def get_expenses_by_date(date1: date, db:Session = Depends(get_db)):
    expense_exist = db.query(Expense).filter(Expense.expense_date==date1).all()

    if not expense_exist:
        raise HTTPException(
            status_code=400,
            detail="No expense on this date"
        )
    return expense_exist
##------------------------------------------------------------------------------------------------------##


@router.get("/total_expense_ofdate/{expense_date}", response_model=ExpenseResponseTotal)
def get_total_expenseoftheday(expense_date: date, db:Session = Depends(get_db)):

    total_expense = db.query(func.sum(Expense.amount)).filter(Expense.expense_date == expense_date).scalar()
    if total_expense is None:
        raise HTTPException(
            status_code=400,
            detail="No expense on this date"
        )
    
    
    return {
        "expense_date" :expense_date,
        "total":float(total_expense) 
    }
##------------------------------------------------------------------------------------------------------##


@router.get("/category_expense/{category_id}",response_model=ExpenseCategoryTotal)
def category_expense_total(category_id: int, db:Session = Depends(get_db)):

    exists = db.query(Category).filter(Category.id == category_id).first()
    if not exists:
        raise HTTPException(
            status_code= 400,
            detail = "Category doesnt exists"
        )
    
    total_expense = db.query(func.sum(Expense.amount)).filter(Expense.category_id == category_id).scalar()
    if total_expense is None:
        total_expense = 0.0

    return {
        "id": category_id,
        "title": exists.name,
        "total": float(total_expense)
    }