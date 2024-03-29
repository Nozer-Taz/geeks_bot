import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()
    

    def sql_create_tables(self):
        if self.connection:
            print('Database created successfully')
        
        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)

        self.connection.commit()

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        sql_queries.INSERT_USER_QUERY,
        (None, tg_id, username, first_name, last_name)
        self.connection.commit()