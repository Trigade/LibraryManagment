class LoansRepository:
    def __init__(self):
        pass

    def add(self, loan, cursor):
        cursor.execute(
            """
                            INSERT INTO loans(loan_date,due_date,return_date,member_id,book_id) VALUES (?,?,?,?,?)
                            """,
            (
                loan.loan_date,
                loan.due_date,
                loan.return_date,
                loan.member_id,
                loan.book_id,
            ),
        )
        return cursor.lastrowid

    def update(self, loan, cursor):
        cursor.execute(
            """
                        UPDATE loans SET loan_date=?,due_date=?,return_date=?,member_id=?,book_id=? WHERE id=?
                        """,
            (
                loan.loan_date,
                loan.due_date,
                loan.return_date,
                loan.member_id,
                loan.book_id,
                loan.id,
            ),
        )
        return cursor.rowcount

    def delete(self, id, cursor):
        cursor.execute(
            """
                            DELETE FROM loans WHERE id=?
                            """,
            (id,),
        )
        return cursor.rowcount

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                SELECT
                loans.loan_id,
                loans.due_date,
                loans.return_date,
                members.first_name,
                members.last_name,
                books.title,
                authors.full_name AS author_name
                FROM loans LEFT JOIN members ON members.id = loans.member_id LEFT JOIN books ON books.id = loans.books_id LEFT JOIN books.author_id = author.id
                WHERE id = ?
                """,
            (id,),
        )
        row = cursor.fetchone()
        return {
                "id":row["id"],
                "due_date":row["due_date"],
                "loan_date":row["loan_date"],
                "return_date":row["return_date"],
                "member_name":row["name"],
                "member_last_name":row["last_name"],
                "title":row["title"],
                "author_name":row["author_name"]
            }


    def get_all(self, cursor):
        cursor.execute(
            """
                SELECT
                loans.id,
                loans.due_date,
                loans.loan_date,
                loans.return_date,
                members.first_name AS name, 
                members.last_name AS last_name,
                books.title AS title,
                authors.full_name AS author_name
                FROM loans LEFT JOIN members ON members.id = loans.member_id LEFT JOIN books ON books.id = loans.book_id LEFT JOIN authors ON books.author_id = authors.id
                """,
        )
        rows = cursor.fetchall()
        loan_list = []
        for row in rows:
            loan = {
                "id":row["id"],
                "due_date":row["due_date"],
                "loan_date":row["loan_date"],
                "return_date":row["return_date"],
                "member_name":row["name"],
                "member_last_name":row["last_name"],
                "book_title":row["title"],
                "author_name":row["author_name"]
            }
            loan_list.append(loan)
        return loan_list