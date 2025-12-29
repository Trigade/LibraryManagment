class FinesRepository:
    def __init__(self):
        pass

    def add(self, fine, cursor):
        cursor.execute(
            """
                            INSERT INTO fines(amount,payment_status,loan_id) VALUES (?,?,?)
                            """,
            (
                fine.amount,
                fine.payment_status,
                fine.loan_id,
            ),
        )
        return cursor.lastrowid

    def update(self, fine, cursor):
        cursor.execute(
            """
                        UPDATE fines SET amount=?,payment_status=?,loan_id=? WHERE id=?
                        """,
            (
                fine.amount,
                fine.payment_status,
                fine.loan_id,
                fine.id,
            ),
        )
        return cursor.rowcount

    def delete(self, id, cursor):
        cursor.execute(
            """
                            DELETE FROM fines WHERE id=?
                            """,
            (id,),
        )
        return cursor.rowcount

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                SELECT 
                fines.id,
                fines.amount,
                fines.payment_status,
                loans.loan_date AS loan_date,
                loans.due_date AS due_date
                FROM fines LEFT JOIN loans ON loans.id = fines.loan_id
                WHERE id = ?
                """,
            (id,),
        )
        row = cursor.fetchone()
        return {
            "id":row["id"],
                "amount":row["amount"],
                "payment":row["payment_status"],
                "loan_id":row["loan_id"]
        } if row else None

    def get_all(self, cursor):
        cursor.execute(
            """
                SELECT 
                fines.id,
                fines.amount,
                fines.payment_status,
                loans.loan_date AS loan_date,
                loans.due_date AS due_date
                FROM fines LEFT JOIN loans ON loans.id = fines.loan_id
                """,
        )
        rows = cursor.fetchall()
        fines_list = []
        for row in rows:
            fine = {
                "id":row["id"],
                "amount":row["amount"],
                "payment":row["payment_status"],
                "loan_id":row["loan_id"]
            }
            fines_list.append(fine)
        return fines_list
