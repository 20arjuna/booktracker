"""
Connect schema to database.
"""
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from models import Base
from sqlalchemy import create_engine

engine = create_engine("sqlite:///books.db", echo=True)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

db = SessionLocal()
db.commit()
db.close()



# 1. Define the asynchronous engine (already done above).
# 2. Create a sessionmaker bound to the engine (already done above, but missing import).
# 3. Initialize the schema by running `create_all` in an async context.

from sqlalchemy.ext.asyncio import AsyncSession

async def init_db():
    async with engine.begin() as conn:
        # import Base from models.py and create all tables in the database
        await conn.run_sync(Base.metadata.create_all)

