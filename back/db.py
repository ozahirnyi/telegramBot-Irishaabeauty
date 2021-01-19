import sqlite3
from sqlite3 import Error, IntegrityError


class Db:
    connection = None

    def __init__(self):
        self.db_connect()

    def db_connect(self):
        try:
            self.connection = sqlite3.connect('donthackmeplease.sqlite')
        except Error:
            print(Error)

    def update_data(self, user_id, tree_value):
        cursor = self.connection.cursor()
        cursor.execute('UPDATE users SET tree_value = %d WHERE user_id = %d' % (tree_value, user_id))
        self.connection.commit()

    def print_db(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        print(cursor.fetchall())

    def insert_data(self, user_id, tree_value):
        try:
            cursor = self.connection.cursor()
            print("Adding")
            cursor.execute('INSERT INTO users VALUES(%d, %d)' % (user_id, tree_value))
            self.connection.commit()
        except IntegrityError:
            self.update_data(user_id, tree_value)

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users('
                       'user_id integer, '
                       'tree_value integer)')
        self.connection.commit()
