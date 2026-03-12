from fastapi import APIRouter, Depends, HTTPException
# APIRouter: lets us group related routes together in one file
# Depends: FastAPI's dependency injection — used to pass in the database session
# HTTPException: lets us return proper HTTP error responses (like 404, 400)
from sqlalchemy.orm import Session
# Session: the SQLAlchemy type for a database session object
from backend_app.database import get_db
# get_db: our dependency function that opens and closes a DB session per request
from backend_app import models, schemas
# models: our SQLAlchemy table definitions (Book, Swipe)
# schemas: our Pydantic request/response shapes (SwipeCreate, SwipeResponse)

router = APIRouter(
    prefix="/swipes",
    # prefix means every route in this file starts with /swipes
    # so @router.post("/") becomes POST /swipes/
    tags=["swipes"]
    # tags group these routes together in the Swagger docs at /docs
)


@router.post("/", response_model=schemas.SwipeResponse)
# @router.post("/") registers this function as a POST /swipes/ endpoint
# response_model=schemas.SwipeResponse tells FastAPI what shape the response will be
# FastAPI uses this to automatically filter and validate the output
def create_swipe(swipe: schemas.SwipeCreate, db: Session = Depends(get_db)):
    # swipe: FastAPI automatically reads the request body and validates it
    #        against SwipeCreate — if it's invalid, FastAPI returns a 422 error
    # db: FastAPI calls get_db() and injects the session here via Depends()

    book = db.query(models.Book).filter(
        models.Book.id == swipe.book_id).first()
    # db.query(models.Book): start a SELECT query on the books table
    # .filter(models.Book.id == swipe.book_id): add a WHERE id = book_id condition
    # .first(): return the first result, or None if no match found
    # SELECT * FROM books WHERE id = 5 LIMIT 1; This is the SQL query that is executed.

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
        # if the book doesn't exist, return a 404 error with a helpful message
        # this prevents swipes from referencing books that don't exist

    db_swipe = models.Swipe(
        # create a new Swipe object — this is NOT saved to the DB yet
        user_id=swipe.user_id,
        # pull user_id from the validated request body
        book_id=swipe.book_id,
        # pull book_id from the validated request body
        action=swipe.action
        # pull action from the validated request body
        # created_at is not set here — PostgreSQL fills it in automatically
    )

    db.add(db_swipe)
    # db.add() stages the new swipe object — tells SQLAlchemy to track it

    db.commit()
    # db.commit() actually writes the staged changes to PostgreSQL
    # nothing is saved until you call commit()

    db.refresh(db_swipe)
    # db.refresh() reloads the object from the database after saving
    # this fills in auto-generated fields like id and created_at
    # without this, db_swipe.id would still be None

    return db_swipe
    # FastAPI takes this SQLAlchemy object, passes it through SwipeResponse,
    # and sends it back to the frontend as JSON
