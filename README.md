# Expense Tracker API

A production-style backend project built using FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and Alembic.

The project is being developed incrementally through multiple versions, with each version introducing new backend engineering concepts and real-world development practices.

Current Version: **V2 – Authentication & Ownership**

---

# Tech Stack

### Backend

* FastAPI
* Python 3.11

### Database

* PostgreSQL

### ORM

* SQLAlchemy

### Authentication

* JWT (JSON Web Tokens)
* Passlib (BCrypt)

### Database Migrations

* Alembic

### Validation

* Pydantic

### Server

* Uvicorn

---

# Features Implemented

## User Authentication

* User Registration
* User Login
* Password Hashing using BCrypt
* JWT Access Token Generation
* JWT Verification
* Protected Routes
* Current User Endpoint (`/auth/me`)

---

## Authorization & Ownership

Every resource belongs to a specific user.

Implemented ownership checks to ensure:

* Users can only view their own expenses
* Users can only modify their own expenses
* Users can only delete their own expenses
* Users can only access their own categories
* Cross-user data access is prevented

---

## Category Management

* Create Category
* Get All Categories
* Get Category By ID
* Update Category
* Delete Category

---

## Expense Management

* Create Expense
* Get All Expenses
* Get Expense By ID
* Update Expense (PUT)
* Partial Update Expense (PATCH)
* Delete Expense

---

## Filtering & Analytics

### Filtering

* Get Expenses By Category
* Get Expenses By Date

### Analytics

* Total Expense By Date
* Total Expense By Category

---

# Database Concepts Used

* One-to-Many Relationships
* Foreign Keys
* Ownership-based Data Isolation
* SQLAlchemy ORM
* Dependency Injection
* PostgreSQL Integration
* Alembic Database Migrations

---

# Security Features

### Password Security

Passwords are never stored in plain text.

* BCrypt Hashing
* Secure Password Verification

### JWT Authentication

Authenticated users receive a signed access token.

Protected endpoints require:

```text
Authorization: Bearer <access_token>
```

### Resource Ownership

Every category and expense is linked to a specific user.

This prevents unauthorized access to another user's data.

---

# Project Structure

```text
Expense_Tracker/
│
├── alembic/
│
├── app/
│
│   ├── auth/
│   │   ├── hashing.py
│   │   ├── jwt_handler.py
│   │   ├── oauth2.py
│   │   └── current_user.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── category.py
│   │   └── expense.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── category.py
│   │   └── expense.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── category.py
│   │   └── expense.py
│   │
│   ├── database.py
│   ├── dependencies.py
│   └── main.py
│
├── alembic.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

# API Endpoints

## Authentication

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /auth/register |
| POST   | /auth/login    |
| GET    | /auth/me       |

---

## Categories

| Method | Endpoint                         |
| ------ | -------------------------------- |
| POST   | /categories                      |
| GET    | /categories                      |
| GET    | /categories/{id}                 |
| PUT    | /categories/update_category/{id} |
| DELETE | /categories/{id}                 |

---

## Expenses

| Method | Endpoint                                       |
| ------ | ---------------------------------------------- |
| POST   | /expenses/add_expense                          |
| GET    | /expenses                                      |
| GET    | /expenses/{expense_id}                         |
| PUT    | /expenses/update_record/{expense_id}           |
| PATCH  | /expenses/update_record_something/{expense_id} |
| DELETE | /expenses/delete/{expense_id}                  |

---

## Analytics

| Method | Endpoint                                        |
| ------ | ----------------------------------------------- |
| GET    | /expenses/get_expense_by_category/{category_id} |
| GET    | /expenses/expense_by_date/{date}                |
| GET    | /expenses/total_expense_ofdate/{expense_date}   |
| GET    | /expenses/category_expense/{category_id}        |

---

# Running Locally

## Clone Repository

```bash
git clone https://github.com/sohamkhore/expense-tracker-api.git
cd expense-tracker-api
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/ExpenseTracker

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Run Migrations

```bash
alembic upgrade head
```

## Start Server

```bash
uvicorn app.main:app --reload
```

---

# Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

# Version Roadmap

## V1 – Core Expense Tracking

* PostgreSQL
* SQLAlchemy ORM
* CRUD APIs
* Relationships
* Filtering
* Aggregations

## V2 – Authentication & Ownership ✅

* User Accounts
* JWT Authentication
* Password Hashing
* Protected Routes
* Resource Ownership
* Alembic Migrations

## V3 – Containerization & Deployment

* Docker
* Docker Compose
* Environment Configuration
* Production Deployment

## V4 – Performance & Scalability

* Redis
* Caching
* Rate Limiting

## V5 – Backend Automation

* Background Jobs
* Scheduled Reports
* Email Notifications

## V6 – Advanced Backend Patterns

* Service Layer
* Repository Pattern
* Logging
* Monitoring
* Testing
* Pagination

---

# Future AI Engineering Roadmap

After completing the backend roadmap, the next focus will be AI engineering projects:

* Resume Analyzer
* RAG Assistant
* Embeddings
* Vector Databases
* LangGraph
* Evaluation & Monitoring

The objective is to transition from backend development into AI engineering while leveraging backend concepts learned through this project.

---

# Author

**Soham Khore**

B.Tech Computer Science Engineering

Backend Development • FastAPI • PostgreSQL • AI Engineering Journey
