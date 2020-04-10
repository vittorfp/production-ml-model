import psycopg2


class PostgresConnection:

    def __init__(self):
        try:
            self._conn = psycopg2.connect(
                user="postgres",
                password="mudar123",
                host="postgres",
                port="5432",
                database="postgres"
            )
        except Exception as error:
            print("Error connecting to Postgres: ", error)

    def query(self, query):
        cursor = self._conn.cursor()
        results = cursor.execute(query)
        cursor.close()
        return results
