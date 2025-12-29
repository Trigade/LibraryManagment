import sqlite3 as sq
import os 

class DbService:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, "library.db")
    SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")

    def get_db_connection(self):
        conn = sq.connect(self.DB_PATH)
        conn.row_factory = sq.Row
        
        return conn

    def initialize_database(self):
        if not os.path.exists(self.SCHEMA_PATH):
            print(f"HATA: '{self.SCHEMA_PATH}' bulunamadı!")
            return

        conn = self.get_db_connection()
        try:
            with open(self.SCHEMA_PATH, 'r', encoding='utf-8') as f:
                schema_script = f.read()
                conn.executescript(schema_script)
                print(f"Veritabanı başarıyla başlatıldı: {self.DB_PATH}")
        except Exception as e:
            print(f"Veritabanı oluşturulurken hata: {e}")
        finally:
            conn.close()