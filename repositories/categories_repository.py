from entities.categories import Categories


class CategoriesRepository:
    def __init__(self):
        pass

    def add(self, category, cursor):
        cursor.execute(
            """
                        INSERT INTO categories(category_name,description) VALUES(?,?)
                            """,
            (
                category.category_name,
                category.description,
            ),
        )
        return cursor.lastrowid

    def update(self, category, cursor):
        cursor.execute(
            """
                        UPDATE categories SET category_name=?,description=? WHERE id=?
                        """,
            (
                category.category_name,
                category.description,
                category.id,
            ),
        )
        return cursor.rowcount

    def delete(self, id, cursor):
        cursor.execute(
            """
                            DELETE FROM categories WHERE id=?
                            """,
            (id,),
        )
        return cursor.rowcount

    def get_by_id(self, id, cursor):
        cursor.execute(
            """
                        SELECT * FROM categories WHERE id=?
                            """,
            (id,),
        )
        row = cursor.fetchone()
        return Categories(
            id=row["id"],
            category_name=row["category_name"],
            description=row["description"],
        ) if row else None

    def get_all(self, cursor):
        cursor.execute("""
                            SELECT * FROM categories
                            """)
        rows = cursor.fetchall()
        categories = []
        for row in rows:
            category = {
                "id":row["id"],
                "category_name":row["category_name"],
                "description":row["description"],
            }
            categories.append(category)
        return categories
    
    def get_entity_by__id():
        pass