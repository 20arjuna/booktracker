'''
Define the physical schema of the database.
'''

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base() # the class that tells sqlalchemy which classes are tables and which are not

class Book(Base):
    __tablename__ = "books"
    book_id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String, nullable=False)
    author_first = sa.Column(sa.String, nullable=False)
    author_last = sa.Column(sa.String, nullable=False)
    year = sa.Column(sa.Integer, nullable=False)
    rating = sa.Column(sa.Decimal, nullable=True)
    comments = sa.Column(sa.Text, nullable=True)
    date_added = sa.Column(sa.DateTime, nullable=False)
    date_completed = sa.Column(sa.DateTime, nullable=True)

