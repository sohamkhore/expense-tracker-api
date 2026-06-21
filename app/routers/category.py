from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

##Post a category
@router.post("/", response_model= CategoryResponse)
def post_category(category: CategoryCreate, db: Session= Depends(get_db)):
    existing = db.query(Category).filter(category.name == Category.name).first()
    if existing :
        raise HTTPException(
            status_code = 400,
            detail= "Category already exists"
        )
    
    new_category = Category(name = category.name)

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

##Get all categories
@router.get("/",response_model= list[CategoryResponse])
def get_all_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()

    return categories

##Get any category by id
@router.get("/{category_id}", response_model= CategoryResponse)
def get_category_by_id( category_id: int, db: Session = Depends(get_db)):

    find_category = db.query(Category).filter(Category.id == category_id).first()

    if not find_category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )
    return find_category

##Delete category by id
@router.delete(
    "/{category_id}"
)
def delete_category(category_id: int,db: Session = Depends(get_db)):

    category = (
        db.query(Category).filter(Category.id == category_id).first()
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    db.delete(category)
    db.commit()
    return {
        "message": "Category deleted successfully"
    }
