from entities.members import Members


class MembersRepository:
    def __init__(self):
        pass

    def add(self, member, cursor):
        cursor.execute(
            """
                INSERT INTO members(first_name, last_name, email, phone) 
                VALUES (?, ?, ?, ?)
                """,
            (member.first_name, member.last_name, member.email, member.phone),
        )
        return cursor.lastrowid

    def update(self, member, cursor):
        cursor.execute(
            """
                        UPDATE members SET first_name=?,last_name = ?,email =?,phone=? WHERE id = ?
                        """,
            (
                member.first_name,
                member.last_name,
                member.email,
                member.phone,
                member.id,
            ),
        )
        return cursor.rowcount

    def delete(self, id, cursor):
        cursor.execute(
            """
                DELETE FROM members WHERE id=?
        """,
            (id,),
        )
        return cursor.rowcount

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                SELECT * FROM members WHERE id = ?
        """,
            (id,),
        )

        row = cursor.fetchone()
        return {
                "id":row["id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email":row["email"],
                "phone":row["phone"],
                "join_date":row["join_date"],
                "membership_status":row["membership_status"]
            } if row else None

    def get_all(self, cursor):
        cursor.execute("""
                        SELECT * FROM members
                """)
        rows = cursor.fetchall()
        members = []
        for row in rows:
            member = {
                "id":row["id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email":row["email"],
                "phone":row["phone"],
                "join_date":row["join_date"],
                "membership_status":row["membership_status"]
                }
            members.append(member)
        return members
