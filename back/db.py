import sqlite3
from sqlite3 import Error


class Db:
    connection = None

    def __init__(self):
        self.db_connect()

    def db_connect(self):
        try:
            self.connection = sqlite3.connect('donthackmeplease.sqlite')
        except Error:
            print(Error)

    def print_db(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        print(cursor.fetchall())

    def get_data(self, user_id):
        cursor = self.connection.cursor()
        print("Getting")
        cursor.execute('SELECT tree_value FROM users WHERE user_id=%d' % user_id)
        print("Before return: %s" % cursor.fetchone())
        return 0 if cursor.fetchone() is None else cursor.fetchone()[0]

    def insert_data(self, user_id, tree_value):
        cursor = self.connection.cursor()
        print("Adding")
        cursor.execute('INSERT OR REPLACE INTO users VALUES(%d, %d)' % (user_id, tree_value))
        self.connection.commit()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users('
                       'user_id integer UNIQUE, '
                       'tree_value integer)')
        self.connection.commit()
