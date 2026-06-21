# Expense Tracker API

A production-style backend project built while learning modern backend development using FastAPI, PostgreSQL, and SQLAlchemy.

Instead of creating multiple small projects, this project is continuously improved through multiple versions, with each version introducing new backend concepts and technologies.

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Pydantic
* Uvicorn

---

## Features Implemented (V1)

### Category Management

* Create Category
* Get All Categories
* Get Category By ID
* Delete Category

### Expense Management

* Create Expense
* Get All Expenses
* Get Expense By ID
* Update Expense (PUT)
* Partial Update Expense (PATCH)
* Delete Expense

### Filtering

* Get Expenses By Category
* Get Expenses By Date

### Summary APIs

* Get Total Expense For A Specific Date
* Get Total Expense For A Specific Category

### Database Concepts Used

* One-to-Many Relationships
* Foreign Keys
* SQLAlchemy ORM
* Dependency Injection
* PostgreSQL Integration

---

## Project Structure

```text
Expense_Tracker/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── dependencies.py
│   │
│   ├── models/
│   │   ├── category.py
│   │   └── expense.py
│   │
│   ├── schemas/
│   │   ├── category.py
│   │   └── expense.py
│   │
│   └── routers/
│       ├── category.py
│       └── expense.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## API Endpoints

### Category APIs

| Method | Endpoint         |
| ------ | ---------------- |
| POST   | /categories      |
| GET    | /categories      |
| GET    | /categories/{id} |
| DELETE | /categories/{id} |

### Expense APIs

| Method | Endpoint                                       |
| ------ | ---------------------------------------------- |
| POST   | /expenses/add_expense                          |
| GET    | /expenses                                      |
| GET    | /expenses/{expense_id}                         |
| PUT    | /expenses/update_record/{expense_id}           |
| PATCH  | /expenses/update_record_something/{expense_id} |
| DELETE | /expenses/delete/{expense_id}                  |

### Filter APIs

| Method | Endpoint                                        |
| ------ | ----------------------------------------------- |
| GET    | /expenses/get_expense_by_category/{category_id} |
| GET    | /expenses/expense_by_date/{date}                |

### Summary APIs

| Method | Endpoint                                      |
| ------ | --------------------------------------------- |
| GET    | /expenses/total_expense_ofdate/{expense_date} |
| GET    | /expenses/category_expense/{category_id}      |

---

## Running Locally

### Clone Repository

```bash
git clone https://github.com/sohamkhore/expense-tracker-api.git
cd expense-tracker-api
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
postgre_URL=YOUR_DATABASE_URL
```

### Start Server

```bash
uvicorn app.main:app --reload
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

## Version Roadmap

### V1 (Current)

* PostgreSQL
* SQLAlchemy ORM
* Relationships
* CRUD APIs
* Filtering
* Aggregations

### V2

* JWT Authentication
* User Accounts
* Password Hashing
* Alembic Migrations

### V3

* Docker
* Deployment

### V4

* Redis
* Caching
* Rate Limiting

### V5

* Background Jobs
* Monthly Report Generation

### Future AI Project

* Resume Analyzer
* RAG Assistant
* Vector Databases
* LangGraph
* Evaluation & Monitoring

---

## Author

Soham Khore

B.Tech Computer Science Engineering
Backend Development & AI Engineering Learning Journey
