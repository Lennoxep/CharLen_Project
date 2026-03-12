"""
Database configuration and connection setup.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get DATABASE_URL from environment variable
# The first argument is the env var name, second is default value
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://lennoxpee@localhost:5432/booktinder")


# Create database engine
# PostgreSQL connection
engine = create_engine(DATABASE_URL)

# Create SessionLocal class for database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create Base class for models
Base = declarative_base()


# Dependency function to get database session
def get_db():
    """
    Dependency function that yields a database session.
    Used with FastAPI's Depends() to inject database sessions into route handlers.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
