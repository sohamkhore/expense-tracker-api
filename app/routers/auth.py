from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserLogin, UserResponse, TokenResponse
from app.models.user import User
from app.dependencies import get_db
from sqlalchemy.orm import Session
from sqlalchemy import DateTime
from datetime import datetime
from app.auth.hashing import hash_password, verify_password
from app.auth.jwt_handler import create_access_token
from app.auth.current_user import get_current_user

router = APIRouter(
    prefix="/auth",
    tags= ["Authentication"]
)

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session=Depends(get_db)):

    
    email_exists = db.query(User).filter(User.email==user.email).first()
    username_exists = db.query(User).filter(User.username == user.username).first()

    if username_exists and email_exists:
        raise HTTPException(
            status_code= 409,
            detail ={
            "email": "already exists",
            "username": "already exists"
            }
        )
    
    if email_exists:
        raise HTTPException(
            status_code= 409,
            detail="Email already exists"
        )
    if username_exists:
        raise HTTPException(
            status_code= 409,
            detail="Username already exists"
        )
    password_hashed = hash_password(user.password)
    new_user= User(
        username= user.username,
        email= user.email,
        password_hash = password_hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model= TokenResponse)
def login_access(data:UserLogin, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.email==data.email).first()

    if not user:
        raise HTTPException(
            status_code = 401,
            detail="Invalid username or password"
        )

    if not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code = 401,
            detail="Invalid email or password"
        )
    
    access_token = create_access_token({
        "sub":str(user.id)
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me",response_model=UserResponse)
def get_me(current_user: User=Depends(get_current_user)):
    return current_user