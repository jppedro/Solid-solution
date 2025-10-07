import sqlite3

class DatabaseManager:
    """Gerencia a conexão e o cursor do banco de dados."""
    def __init__(self, db_name: str):
        self._db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        """Abre a conexão com o banco de dados ao entrar no contexto."""
        self.conn = sqlite3.connect(self._db_name)
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Fecha a conexão, commitando as alterações ou revertendo em caso de erro."""
        if exc_type is None:
            self.conn.commit()
        self.conn.close()

    def _create_table_if_not_exists(self):
        """Cria a tabela de pedidos se ela não existir."""
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