CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL,
    description CHAR(1000)
);

CREATE TABLE IF NOT EXISTS publishers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(20),
    address VARCHAR(100),
    phone VARCHAR(20) UNIQUE
);

CREATE TABLE IF NOT EXISTS members(
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    join_date DATE DEFAULT CURRENT_DATE,
    membership_status VARCHAR(20) DEFAULT 'Active'
);

CREATE TABLE IF NOT EXISTS staff(
    id INTEGER PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE
);

CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY,
    full_name VARCHAR(50) NOT NULL UNIQUE,
    biography VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title VARCHAR(100),
    isbn VARCHAR(24) UNIQUE,
    publish_year INTEGER,
    stock_quantity INTEGER DEFAULT 0,
    author_id INTEGER,
    publisher_id INTEGER,
    category_id INTEGER,
    FOREIGN KEY (publisher_id) REFERENCES publishers(id),
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY,
    loan_date DATE,
    due_date DATE,
    return_date DATE,
    member_id INTEGER,
    book_id INTEGER,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);

CREATE TABLE IF NOT EXISTS fines (
    id INTEGER PRIMARY KEY,
    amount INTEGER,
    payment_status INTEGER DEFAULT 0,
    loan_id INTEGER,
    FOREIGN KEY (loan_id) REFERENCES loans(id)
);