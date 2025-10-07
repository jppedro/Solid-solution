import sqlite3

class DatabaseManager:
    def __init__(self, db_name: str):
        self._db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self._db_name)
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        self.conn.close()

    def _create_table_if_not_exists(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                customer_name TEXT,
                customer_type TEXT,
                items TEXT,
                total_price REAL,
                status TEXT,
                created_at TEXT
            )
        """)
        self.conn.commit()