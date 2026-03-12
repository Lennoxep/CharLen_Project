from fastapi import FastAPI
# imports fastAPI library
from fastapi.middleware.cors import CORSMiddleware
# helps the frontend to call the backend
from backend_app.database import engine
from backend_app import models
from backend_app.routes import books, swipes
# swipes is new — import the swipes router the same way you imported books

models.Base.metadata.create_all(bind=engine)
# this scans all models (Book, Swipe) and creates any missing tables in PostgreSQL
# now that Swipe exists in models.py, running the server will auto-create the swipes table

app = FastAPI(title="CharLen_Project API", version="0.1.0")

# CORS: allows your React frontend to call this backend
app.add_middleware(
    # middleware is code that sits between the incoming request and the outgoing response
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite default
        "http://localhost:3000",  # if you ever switch setups
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "BookTinder backend is running"}


app.include_router(books.router)
app.include_router(swipes.router)
# include_router registers all the routes from swipes.py into the main app
# without this line, POST /swipes/ would not exist even if the file is perfect


@app.get("/health")
def health():
    return {"status": "ok"}
