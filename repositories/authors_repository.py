from entities.authors import Authors


class AuthorsRepository:
    def __init__(self):
        pass

    def add(self, author, cursor):
        cursor.execute(
            """
                            INSERT INTO authors(full_name,biography) VALUES (?,?)
                            """,
            (
                author.full_name,
                author.biography,
            ),
        )
        return cursor.lastrowid

    def update(self, author, cursor):
        cursor.execute(
            """
                        UPDATE authors SET full_name = ?,biography=? WHERE id = ?
                    """,
            (
                author.full_name,
                author.biography,
                author.id,
            ),
        )
        return cursor.rowcount

    def delete(self, id, cursor):
        cursor.execute(
            """
                            DELETE FROM authors WHERE id=?
                            """,
            (id,),
        )
        return cursor.rowcount

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                            SELECT * FROM authors WHERE id=?
                            """,
            (id,),
        )
        row = cursor.fetchone()
        return Authors(
            id=row["id"],
            full_name=row["full_name"],
            biography=row["biography"],
        ) if row else None

    def get_all(self, cursor):
        cursor.execute("""
                            SELECT * FROM authors
                            """)
        rows = cursor.fetchall()
        authors = []
        for row in rows:
            author = {
                "id":row["id"],
                "full_name":row["full_name"],
                "biography":row["biography"],
            }
            authors.append(author)
        return authors

