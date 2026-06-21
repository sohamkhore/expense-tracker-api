from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base

import os
from dotenv import load_dotenv
load_dotenv()

URL = os.getenv("postgre_URL")
engine = create_engine(URL, echo=True)

SessionLocal = sessionmaker(autoflush=False, autocommit = False , bind= engine)

Base = declarative_base()
