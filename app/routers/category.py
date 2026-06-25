from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.auth.current_user import get_current_user
from app.models.category import Category
from app.models.user import User
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)
##------------------------------------------------------------------------------------------------------##

##Post a category
@router.post("/", response_model= CategoryResponse)
def post_category(
    category: CategoryCreate, 
    db: Session= Depends(get_db), 
    current_user :User=Depends(get_current_user)
    ):
    existing = db.query(Category).filter(Category.name==category.name, Category.user_id == current_user.id).first()
    if existing :
        raise HTTPException(
            status_code = 400,
            detail= "Category already exists"
        )
    
    new_category = Category(
                        name = category.name,
                        user_id = current_user.id
                        )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category
##------------------------------------------------------------------------------------------------------##


##Get all categories
@router.get("/",response_model= list[CategoryResponse])
def get_all_categories(
    db: Session = Depends(get_db),
    current_user: User=Depends(get_current_user)
    ):
    categories = db.query(Category).filter(Category.user_id==current_user.id).all()

    return categories
##------------------------------------------------------------------------------------------------------##

##Get any category by id
@router.get("/{category_id}", response_model= CategoryResponse)
def get_category_by_id( 
    category_id: int, 
    db: Session = Depends(get_db),
    current_user: User=Depends(get_current_user)
    ):

    find_category = db.query(Category).filter(Category.id == category_id, Category.user_id==current_user.id).first()

    if not find_category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )
    return find_category
##------------------------------------------------------------------------------------------------------##


##Delete category by id
@router.delete(
    "/{category_id}"
)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User=Depends(get_current_user)
    ):

    category = (
        db.query(Category).filter(Category.id == category_id,Category.user_id==current_user.id).first()
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
##------------------------------------------------------------------------------------------------------##


##Update a category
@router.put("/update_category/{category_id}",response_model=CategoryResponse)
def update_category(
        category: CategoryCreate, 
        category_id: int,
        db:Session=Depends(get_db), 
        current_user :User=Depends(get_current_user)
        ):
    category_exist = db.query(Category).filter(Category.id == category_id, Category.user_id == current_user.id).first()

    if not category_exist:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )
    
    existing = db.query(Category).filter(Category.name == category.name,Category.user_id == current_user.id,Category.id != category_id).first()

    if existing:
        raise HTTPException(
        status_code=400,
        detail="Category already exists"
        )

    category_exist.name = category.name

    db.commit()
    db.refresh(category_exist)

    return category_exist