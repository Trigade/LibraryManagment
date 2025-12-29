from entities.books import Books


class BooksRepository:
    def __init__(self):
        pass

    def add(self, book, cursor) -> int:
        cursor.execute(
            """
                INSERT INTO books(title,isbn,publish_year,stock_quantity,publisher_id,category_id,author_id) VALUES(?,?,?,?,?,?,?) 
            """,
            (
                book.title,
                book.isbn,
                book.publish_year,
                book.stock_quantity,
                book.publisher_id,
                book.category_id,
                book.author_id,
            ),
        )
        return cursor.lastrowid

    def update(self, book, cursor) -> int:
        cursor.execute(
            """
                        UPDATE books SET title=?,isbn=?,publish_year=?,stock_quantity=?,publisher_id=?,category_id=?,author_id=? WHERE id=?
                        """,
            (
                book.title,
                book.isbn,
                book.publish_year,
                book.stock_quantity,
                book.publisher_id,
                book.category_id,
                book.author_id,
                book.id,
            ),
        )
        return cursor.rowcount

    def delete(self, id, cursor) -> int:
        cursor.execute(
            """
                DELETE FROM books WHERE id=?
        """,
            (id,),
        )
        return cursor.rowcount

    def get_by_id(self, id, cursor) -> dict | None:
        cursor.execute(
            """
                SELECT books.id, 
                books.title, 
                books.isbn, 
                books.publish_year, 
                books.stock_quantity,
                books.publisher_id,
                books.category_id,
                books.author_id,
                publishers.name AS publisher_name,
                categories.category_name AS category_name, 
                authors.full_name AS author_name FROM books LEFT JOIN publishers ON publishers.id=books.publisher_id LEFT JOIN categories ON categories.id=books.category_id LEFT JOIN authors ON authors.id=books.author_id WHERE books.id=?
            """,
            (id,),
        )
        book = cursor.fetchone()
        return {
            "id": book[0],
            "title": book[1],
            "isbn": book[2],
            "publish_year": book[3],
            "stock_quantity": book[4],
            "publisher_name": book[5],
            "category_name": book[6],
            "author_name": book[7],
        } if book else None

    def get_all(self, cursor) -> list[dict]:
        cursor.execute("""
                SELECT books.id, 
                books.title, 
                books.isbn, 
                books.publish_year, 
                books.stock_quantity,
                publishers.name AS publisher_name,
                categories.category_name AS category_name, 
                authors.full_name AS author_name
                FROM books LEFT JOIN publishers ON publishers.id=books.publisher_id LEFT JOIN categories ON categories.id=books.category_id LEFT JOIN authors ON authors.id=books.author_id
            """)
        rows = cursor.fetchall()
        book_list = []
        for row in rows:
            book = {
                "id": row["id"],
                "title": row["title"],
                "isbn": row["isbn"],
                "publish_year": row["publish_year"],
                "stock_quantity": row["stock_quantity"],
                "publisher_name": row["publisher_name"],
                "category_name": row["category_name"],
                "author_name": row["author_name"],
            }
            book_list.append(book)
        return book_list

    def increase_stock(self,id,cursor):
        cursor.execute("""
                        UPDATE books SET stock_quantity = stock_quantity + 1 WHERE id = ?
                        """,
                        (id,)
        )
        return cursor.rowcount

    def get_by_isbn(self, isbn, cursor) -> dict | None:
        cursor.execute(
            """
                SELECT  
                books.isbn,
                books.id
                FROM books WHERE books.isbn=?
            """,
            (isbn,)
        )
        book = cursor.fetchone()
        return {
            "isbn": book["isbn"],
            "id":book["id"]
        } if book else None