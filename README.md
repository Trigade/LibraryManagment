#Library Management System (LMS)A modular, Python-based Library Management System designed to handle core library operations such as managing books, authors, members, and loans. This project uses **SQLite** for data persistence and follows a layered architecture separating entities, repositories, and services.

##Project Structure The project is organized into the following directories:

* **`core/entities/`**: Contains Python classes representing the data models (e.g., `Books`, `Authors`, `Loans`, `Members`).
* **`database/`**: Handles database connections and initialization.
* `db_service.py`: Script to connect to SQLite and run the initial schema.
* `schema.sql`: SQL commands to create the necessary tables.
* `library.db`: The SQLite database file (generated automatically).


* **`repositories/`**: The Data Access Layer (DAL). Contains classes like `BooksRepository` that execute raw SQL queries.
* **`services/`**: The Business Logic Layer. Classes like `BooksService` that bridge the gap between the main application and the repositories.
* **`main.py`**: The entry point of the application.

##Features* **Book Management**: Add, delete, and retrieve book information.
* **Database Integration**: Automatic SQLite database initialization using a predefined SQL schema.
* **Entity-Relationship Model**: Includes tables for Categories, Publishers, Members, Staff, Authors, Loans, and Fines.
* **Clean Architecture**: Separation of concerns between data storage (Repositories) and logic (Services).

##🛠️ Prerequisites* Python 3.x
* SQLite3 (Standard in most Python installations)

##📥 Installation & Setup1. **Clone the repository** (or download the files):
```bash
git clone <repository-url>
cd trigade/lms

```


2. **Verify the directory structure**:
Ensure `schema.sql` is present inside the `database/` folder so the application can initialize the tables.
3. **Run the Application**:
Execute the `main.py` file to start the system.
```bash
python main.py

```

##UsageWhen you run `main.py`, the system performs the following steps automatically:

1. **Initialize Database**: Checks for `library.db`. If it doesn't exist, it creates it using `database/schema.sql`.
2. **Register a Book**: The current sample code creates a `Books` object and saves it to the database via `BooksService`.
3. **Retrieve Data**: It fetches and prints the details of the book with ID `1` to the console.

###Example Code (`main.py`)```python
from database.db_service import DbService
from core.entities.books import Books
from services.books_service import BooksService
from repositories.books_repository import BooksRepository

# Initialize DB
db_service = DbService()
db_service.initialize_database()
conn = db_service.get_db_connection()

# Create and Add a Book
new_book = Books("Atakan", "123456", 2025, 5, 242, 1)
book_repository = BooksRepository(conn)
book_service = BooksService(book_repository)
book_service.add_book(new_book)

# Fetch and Print Result
print(book_service.get_book(1))

```

##Database SchemaThe system includes the following main tables:

* `books`: Stores title, ISBN, year, stock, publisher, and category.
* `authors` & `book_authors`: Manage book authorship.
* `members`: Stores library member details.
* `loans` & `fines`: Tracks borrowed books and overdue payments.
* `publishers` & `categories`: Metadata for books.
