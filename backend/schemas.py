from pydantic import BaseModel

# parent class for all books
class BookBase(BaseModel):
    title: str
    author_first: str
    author_last: str
    year: int
    rating: float | None = None
    comments: str | None = None
    date_added: datetime | None = None
    date_completed: datetime | None = None

# serializes post requests
class BookCreate(BookBase):
    pass

# serializes patch requests. doesn't override bookbase
class BookUpdate(BaseModel):
    title: str | None = None
    author_first: str | None = None
    author_last: str | None = None
    year: int | None = None
    rating: float | None = None
    comments: str | None = None
    date_added: datetime | None = None
    date_completed: datetime | None = None

class BookOutput(BookBase):
    # inherits all fields from bookbase
    book_id: int

    # converts sqlalchemy to json
    class Config:
        orm_mode = True