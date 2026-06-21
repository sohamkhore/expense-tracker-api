from fastapi import FastAPI
from app.database import engine,Base
from app.models.expense import Expense
from app.models.category import Category

from app.routers.category import router as category_router
from app.routers.expense import router as expense_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(category_router)
app.include_router(expense_router)

@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}