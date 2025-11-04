from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal, engine
from models import Book
from typing import List
import schemas
import uvicorn

app = FastAPI(title="Book Tracker", description="Personal book tracking app.")

# gives database connection to each route and closes it after the route is done.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --ROUTES--

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/books", response_model=List[schemas.BookOutput])
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books

@app.get("/books/{book_id}", response_model=schemas.BookOutput)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.book_id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=schemas.BookOutput)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = Book(
        title=book.title,
        author_first=book.author_first,
        author_last=book.author_last,
        year=book.year,
    )
    db.add(db_book)
    db.commit() # commits the book to the database
    db.refresh(db_book) # updates the book with the new id
    return db_book

@app.patch("/books/{book_id}", response_model=schemas.BookOutput)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.book_id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for field, value in book.model_dump(exclude_unset=True).items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.book_id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Try a simple query against the database
        db.execute("SELECT 1")
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}






if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)