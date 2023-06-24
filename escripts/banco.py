import pprint
import urllib.parse

import psycopg2


class ClienteBanco:

    def __init__(self, db_url):
        self.db_url = db_url
        self.conn = None

    def conectar(self):
        if self.conn is None or self.conn.closed:
            config = urllib.parse.urlparse(self.db_url)
            config = dict(
                user=config.username,
                password=config.password,
                host=config.hostname,
                port=config.port,
                database=config.path[1:],
            )
            self.conn = psycopg2.connect(**config)

    def executar(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            for linha in cursor.fetchall():
                pprint.pprint(linha)

    def __enter__(self):
        self.conectar()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.conn:
            self.conn.close()

        if exc_tb is not None:
            print('Um erro ocorreu durante o processamento.', exc_type, exc_value, exc_tb)
            return True
