# user_model.py

import psycopg2
from psycopg2 import sql

class UserModel:
    def __init__(self, db_config):
        self.db_config = db_config

    def authenticate_user(self, username, password):
        conn = psycopg2.connect(**self.db_config)
        cur = conn.cursor()

        try:
            # query = sql.SQL("SELECT * FROM users WHERE username = {} AND password = {}").format(
            #     sql.Identifier(username), sql.Identifier(password)
            # )
            queryText = "SELECT * FROM users WHERE username = '"+username+"' AND password = '"+password+"'"
            query = sql.SQL(queryText)
            print(f"Executing SQL query: {query}")
            cur.execute(query)

            return cur.fetchone() is not None

        finally:
            cur.close()
            conn.close()
