"""
Connect schema to database.
"""
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from models import Base
from sqlalchemy import create_engine

engine = create_engine("sqlite:///books.db", echo=True)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

db = SessionLocal()

db.commit()
db.close()





