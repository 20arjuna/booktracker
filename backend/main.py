from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal, engine
from models import Book
from typing import List

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





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)