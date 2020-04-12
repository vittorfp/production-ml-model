import os
import psycopg2


class PostgresConnection:

    def __init__(self):
        self.host = os.getenv('PG_HOST', "postgres")
        self.user = os.getenv('PG_USER', 'postgres')
        self.password = os.getenv('PG_PASS', 'mudar123')
        self.port = os.getenv('PG_PORT', 5432)
        self.db = os.getenv('PG_DB', 'postgres')
        self._conn = self.connect()

    def connect(self):
        try:
            return psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.db,
                connect_timeout=3
            )
        except Exception as error:
            print("Error connecting to Postgres: ", error)
            raise error

    def query(self, query):
        if self._conn.closed:
            self._conn = self.connect()

        cursor = self._conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        self._conn.commit()
        return results
