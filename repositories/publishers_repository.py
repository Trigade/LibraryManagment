

from entities.publishers import Publisher


class PublishersRepository:
    def __init__(self):
        pass

    def add(self, publisher, cursor):
        cursor.execute(
            """
                    INSERT INTO publishers(name,address,phone) VALUES (?,?,?)
                        """,
            (
                publisher.name,
                publisher.address,
                publisher.phone,
            ),
        )
        return cursor.lastrowid

    def update(self, publisher, cursor):
        cursor.execute(
            """
                    UPDATE publishers SET name=?,address=?,phone=?  WHERE id=?
                        """,
            (
                publisher.name,
                publisher.address,
                publisher.phone,
                publisher.id,
            ),
        )
        return cursor.rowcount

    def delete(self, id, cursor):
        cursor.execute(
            """
                DELETE FROM publishers WHERE id=?
        """,
            (id,),
        )
        return cursor.rowcount

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                        SELECT * FROM publishers WHERE id=?
                            """,
            (id,),
        )
        row = cursor.fetchone()
        return Publisher(
            id=row["id"],
            name=row["name"],
            address=row["address"],
            phone=row["phone"],
        ) if row else None

    def get_all(self, cursor):
        cursor.execute("""
                            SELECT * FROM publishers
                            """)
        rows = cursor.fetchall()
        publishers = []
        for row in rows:
            publisher = Publisher(
                id=row[0],
                name=row[1],
                address=row[2],
                phone=row[3],
            )
            publishers.append(publisher)
        return publishers

