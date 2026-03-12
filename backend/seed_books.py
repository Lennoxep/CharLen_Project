"""
Seed script — populates the books table with real book data from the Open Library API.

WHY A SEED SCRIPT?
    A "seed script" is a standalone file you run ONCE to fill your database with starter data.
    Instead of manually typing INSERT statements in psql, this script does it automatically.
    It's a common pattern in web development — almost every project has one.

HOW IT WORKS:
    1. We have a list of popular book ISBNs (a book's unique barcode number)
    2. For each ISBN, we call the Open Library API to get the book's details
    3. We save each book into our PostgreSQL database using SQLAlchemy

HOW TO RUN:
    cd backend
    source venv/bin/activate
    pip install requests          (if not already installed)
    python seed_books.py
"""

import requests
# "requests" is a Python library for making HTTP calls (talking to websites/APIs)
# We use it to call the Open Library API and get book data back
# Think of it like your code opening a browser and visiting a URL, then reading the page

import sys
# "sys" is a built-in Python module that gives us access to system-level functions
# We use sys.exit() to stop the script early if something goes wrong

from backend_app.database import SessionLocal, engine
# SessionLocal: our session factory — creates database connections
# engine: the main connection to PostgreSQL (needed to create tables)

from backend_app.models import Book, Base
# Book: our SQLAlchemy model — represents the books table
# Base: needed to create tables if they don't exist yet


# ──────────────────────────────────────────────
# STEP 1: Define the books we want to seed
# ──────────────────────────────────────────────
# Each entry is a tuple: (ISBN, genre)
# ISBN = International Standard Book Number — a unique ID for every published book
# We provide the genre manually because Open Library's genre data is inconsistent
# A TUPLE is like a list, but it can't be changed after creation — written with ()
# A LIST can be changed after creation — written with []
# We use a list of tuples here because we want the list to be flexible,
# but each (ISBN, genre) pair should stay fixed together

BOOKS_TO_SEED = [
    # ── Fiction / Classics ──
    ("9780743273565", "Fiction"),          # The Great Gatsby
    ("9780061120084", "Fiction"),          # To Kill a Mockingbird
    ("9780451524935", "Fiction"),          # 1984
    ("9780141439518", "Fiction"),          # Pride and Prejudice
    ("9780142437209", "Fiction"),          # Of Mice and Men

    # ── Fantasy ──
    ("9780547928227", "Fantasy"),          # The Hobbit
    ("9780439554930", "Fantasy"),          # Harry Potter and the Sorcerer's Stone
    ("9780553573404", "Fantasy"),          # A Game of Thrones
    ("9780618640157", "Fantasy"),          # The Lord of the Rings
    ("9780062315007", "Fantasy"),          # The Alchemist

    # ── Science Fiction ──
    ("9780441172719", "Science Fiction"),  # Dune
    ("9780345391803", "Science Fiction"),  # The Hitchhiker's Guide to the Galaxy
    ("9780553293357", "Science Fiction"),  # Foundation
    ("9780812550702", "Science Fiction"),  # Ender's Game
    ("9780060850524", "Science Fiction"),  # Brave New World

    # ── Mystery / Thriller ──
    ("9780307474278", "Mystery"),          # The Girl with the Dragon Tattoo
    ("9780062024039", "Thriller"),         # Killing Floor (Jack Reacher)
    ("9780525478812", "Thriller"),         # The Girl on the Train

    # ── Romance ──
    ("9780062457714", "Romance"),          # The Notebook
    ("9780061240089", "Romance"),          # Me Before You

    # ── Non-Fiction ──
    ("9780307887436", "Non-Fiction"),      # Thinking, Fast and Slow
    ("9780062316110", "Non-Fiction"),      # Sapiens
    ("9780374533557", "Non-Fiction"),      # Thinking, Fast and Slow (alt)
    ("9780062457738", "Self-Help"),        # The Subtle Art of Not Giving a F*ck

    # ── Horror ──
    ("9780307743657", "Horror"),           # The Shining
]


# ──────────────────────────────────────────────
# STEP 2: Define a function to fetch book data from Open Library
# ──────────────────────────────────────────────
# WHY A FUNCTION?
#   We need to do the same thing (fetch data from API) for each book.
#   Instead of copy-pasting the same code 25 times, we write it ONCE in a function
#   and CALL it 25 times with different ISBNs. This is called DRY: Don't Repeat Yourself.
#
# PARAMETERS:
#   isbn (str): the book's ISBN number, like "9780743273565"
#   genre (str): the genre we want to assign, like "Fiction"
#
# RETURNS:
#   A dictionary with the book's details, or None if the API call failed

def fetch_book_from_openlibrary(isbn, genre):
    """
    Calls the Open Library API to get a book's title, author, description,
    and cover image using its ISBN.
    
    Returns a dictionary with the book data, or None if the book wasn't found.
    """

    # ── Build the API URL ──
    # f-strings let you put variables inside a string using {curly braces}
    # This URL asks Open Library: "Give me info about the book with this ISBN"
    url = f"https://openlibrary.org/isbn/{isbn}.json"

    # ── Make the HTTP request ──
    # requests.get(url) sends a GET request to the URL (like visiting it in a browser)
    # The response comes back as an object with status codes and data
    try:
        response = requests.get(url, timeout=10)
        # timeout=10 means "if the API doesn't respond within 10 seconds, give up"
        # without a timeout, your script could hang forever if the API is down
    except requests.exceptions.RequestException as e:
        # "except" catches any errors that happen during the request
        # (e.g., no internet, API is down, DNS failure)
        # "as e" stores the error details in a variable called "e"
        print(f"  Network error for ISBN {isbn}: {e}")
        return None
        # return None means "I couldn't get this book, skip it"

    # ── Check if the API found the book ──
    # HTTP status code 200 means "success" — the API found the book
    # Any other code (404, 500, etc.) means something went wrong
    if response.status_code != 200:
        print(f"  ISBN {isbn} not found (HTTP {response.status_code})")
        return None

    # ── Parse the JSON response ──
    # .json() converts the API's text response into a Python dictionary
    # A dictionary is like a labeled box: {"title": "The Great Gatsby", "authors": [...]}
    data = response.json()

    # ── Extract the title ──
    # .get("title", "Unknown Title") means:
    # "Look for the key 'title' in the dictionary. If it's not there, use 'Unknown Title'"
    # This prevents a crash if the API response is missing the title field
    title = data.get("title", "Unknown Title")

    # ── Extract the description ──
    # Descriptions in Open Library can be either:
    #   - A plain string: "A story about..."
    #   - A dictionary: {"type": "/type/text", "value": "A story about..."}
    # So we need to handle both formats
    description_raw = data.get("description", "No description available.")
    # isinstance() checks what TYPE a variable is
    # isinstance(description_raw, dict) asks: "Is this a dictionary?"
    if isinstance(description_raw, dict):
        # If it's a dictionary, the actual text is inside the "value" key
        description = description_raw.get("value", "No description available.")
    else:
        # If it's already a string, use it directly
        description = description_raw

    # ── Build the cover image URL ──
    # Open Library provides cover images at a predictable URL pattern
    # You just need the ISBN and the size (S=small, M=medium, L=large)
    # We use L for large, high-quality cover images
    cover_image = f"https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg"

    # ── Fetch the author name ──
    # Open Library stores authors separately — the book data only has author REFERENCES
    # data.get("authors", []) gets the list of author references, or an empty list if none
    author_name = "Unknown Author"
    # default value in case we can't find the author
    authors_list = data.get("authors", [])
    # authors_list looks like: [{"key": "/authors/OL12345A"}]
    # Each entry has a "key" which is a PATH to the author's page on Open Library

    if authors_list:
        # if the list is not empty (has at least one author)
        # [0] gets the FIRST author (index 0 — lists start counting at 0)
        author_key = authors_list[0].get("key", "")
        # author_key looks like: "/authors/OL12345A"

        if author_key:
            # Now we make a SECOND API call to get the author's actual name
            author_url = f"https://openlibrary.org{author_key}.json"
            try:
                author_response = requests.get(author_url, timeout=10)
                if author_response.status_code == 200:
                    author_data = author_response.json()
                    author_name = author_data.get("name", "Unknown Author")
            except requests.exceptions.RequestException:
                # If the author API call fails, we just keep "Unknown Author"
                pass
                # "pass" means "do nothing" — it's a placeholder
                # we use it here because we don't want to crash the whole script
                # just because one author lookup failed

    # ── Return the book data as a dictionary ──
    # We return a dictionary so the calling code can easily access each field by name
    # This is a common pattern: functions return structured data, not raw strings
    return {
        "title": title,
        "author": author_name,
        "description": description,
        "cover_image": cover_image,
        "genre": genre,
    }


# ──────────────────────────────────────────────
# STEP 3: Main script — run the seeding process
# ──────────────────────────────────────────────
# WHY if __name__ == "__main__"?
#   This is a Python convention. It means:
#   "Only run this code if this file is executed directly (python seed_books.py)"
#   "Do NOT run this code if this file is imported by another file"
#   In an interview, you'd explain: "It prevents side effects when importing."

if __name__ == "__main__":

    print("🌱 Starting book seeding process...\n")

    # ── Create tables if they don't exist ──
    # Base.metadata.create_all(bind=engine) looks at all your models (Book, Swipe)
    # and creates the corresponding tables in PostgreSQL if they're not already there
    # This is SAFE to run multiple times — it won't delete existing data
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables verified.\n")

    # ── Open a database session ──
    # SessionLocal() creates a new session — a connection to the database
    # We use this session to add books and save them
    db = SessionLocal()

    # ── Track how many books we add ──
    # We use counters to show a summary at the end
    added_count = 0
    # counts how many NEW books were added
    skipped_count = 0
    # counts how many books were already in the database (duplicates)
    failed_count = 0
    # counts how many books we couldn't fetch from the API

    # ── Loop through each book ──
    # A FOR LOOP runs the same block of code once for each item in a list
    # "for isbn, genre in BOOKS_TO_SEED" means:
    #   - Take each tuple from the list
    #   - Unpack it into two variables: isbn and genre
    #   - Run the indented code below for each one
    # This is called "tuple unpacking" — Python splits ("9780743273565", "Fiction")
    # into isbn="9780743273565" and genre="Fiction" automatically

    for isbn, genre in BOOKS_TO_SEED:
        print(f"📖 Processing ISBN: {isbn}...")

        # ── Check for duplicates ──
        # Before adding a book, check if it's already in the database
        # We search the books table for any book whose cover_image URL contains this ISBN
        # .filter() adds a WHERE clause, .first() gets the first match (or None)
        existing_book = db.query(Book).filter(
            Book.cover_image.contains(isbn)
        ).first()
        # .contains(isbn) generates SQL: WHERE cover_image LIKE '%9780743273565%'
        # This works because our cover URLs always include the ISBN

        if existing_book:
            # If a book with this ISBN already exists, skip it
            print(f"  ⏭️  Already exists: {existing_book.title}")
            skipped_count += 1
            # += 1 is shorthand for: skipped_count = skipped_count + 1
            continue
            # "continue" means "skip the rest of this loop iteration and go to the next one"
            # without continue, the code below would still run and try to add a duplicate

        # ── Fetch book data from Open Library ──
        book_data = fetch_book_from_openlibrary(isbn, genre)
        # This calls our function from Step 2
        # It returns a dictionary with the book's details, or None if it failed

        if book_data is None:
            # The API call failed — skip this book
            failed_count += 1
            continue

        # ── Create a new Book object and add it to the database ──
        # This is the same pattern you saw in swipes.py:
        #   1. Create an instance of the model
        #   2. Add it to the session
        #   3. Commit (save) the session
        new_book = Book(
            title=book_data["title"],
            author=book_data["author"],
            description=book_data["description"],
            cover_image=book_data["cover_image"],
            genre=book_data["genre"],
        )
        # Book(...) creates a new Book object in memory (NOT in the database yet)
        # We pass in each field using the data we got from the API

        db.add(new_book)
        # db.add() tells SQLAlchemy: "I want to save this object to the database"
        # But it's not saved yet — it's just staged (like git add before git commit)

        print(f"  ✅ Added: {book_data['title']} by {book_data['author']}")
        added_count += 1

    # ── Save all changes at once ──
    # db.commit() writes ALL the staged books to PostgreSQL in one batch
    # WHY commit once at the end instead of after each book?
    #   - It's FASTER — one big database write instead of 25 small ones
    #   - It's SAFER — if something fails, none of the books are saved (all or nothing)
    #   This is called a "transaction" — a group of changes that succeed or fail together
    try:
        db.commit()
        print(f"\n✅ Seeding complete!")
    except Exception as e:
        # If the commit fails, undo all changes
        db.rollback()
        # rollback() reverses all staged changes — nothing gets saved
        print(f"\n❌ Error saving to database: {e}")
        sys.exit(1)
        # sys.exit(1) stops the script with exit code 1 (meaning "error")
        # exit code 0 means "success", any other number means "something went wrong"
    finally:
        # "finally" runs no matter what — whether commit succeeded or failed
        db.close()
        # Always close the database session when you're done
        # This frees up the connection for other processes

    # ── Print summary ──
    print(f"   📚 Added:   {added_count} books")
    print(f"   ⏭️  Skipped: {skipped_count} (already existed)")
    print(f"   ❌ Failed:  {failed_count} (API errors)")
    print(f"\n🎉 Your database now has real books with cover images!")
    print(f"   Start your server (uvicorn backend_app.main:app --reload)")
    print(f"   and visit http://localhost:8000/books/ to see them.")
