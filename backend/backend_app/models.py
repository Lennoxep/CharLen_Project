from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
# DateTime is new — we need it to record when the swipe happened
from sqlalchemy.sql import func
# func gives us access to SQL functions like func.now() for auto-timestamps
from .database import Base


class Book(Base):
    __tablename__ = "books"
    # number that acts as a unique identifier for the book, (index=true) allows for faster lookups and searches.
    id = Column(Integer, primary_key=True, index=True)
    # title of the book, (nullable=false) means that the title is required and cannot be empty.
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    cover_image = Column(String)  # url of the book's cover image.
    genre = Column(String)  # genre of the book.


class Swipe(Base):
    # Base is the parent class from SQLAlchemy that turns this Python class into a database table
    __tablename__ = "swipes"
    # __tablename__ tells SQLAlchemy what to name the table in PostgreSQL

    id = Column(Integer, primary_key=True, index=True)
    # id: every row needs a unique identifier
    # primary_key=True means this is the main identifier for each row
    # index=True speeds up lookups when searching by id

    user_id = Column(Integer, nullable=False)
    # user_id: which user performed the swipe
    # Integer because user IDs will be numbers
    # nullable=False means every swipe MUST have a user — you can't swipe anonymously
    # note: we'll add a ForeignKey to the users table in Milestone 5 when users exist

    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    # book_id: which book was swiped on
    # ForeignKey("books.id") links this column to the id column in the books table
    # this enforces referential integrity — you can't swipe on a book that doesn't exist
    # nullable=False means every swipe must be on a real book

    action = Column(String, nullable=False)
    # action: stores either "like" or "dislike"
    # String because it's a text value, not a number
    # nullable=False means the action is required — every swipe must be a like or dislike

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # created_at: timestamp of when the swipe happened
    # DateTime(timezone=True) stores the date and time with timezone info
    # server_default=func.now() means PostgreSQL automatically fills this in
    # when a new row is inserted — you don't have to pass it manually
