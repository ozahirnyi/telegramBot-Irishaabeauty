import sqlite3
from sqlite3 import Error


class Db:
    connection = None

    def __init__(self):
        self.db_connect()

    def db_connect(self):
        try:
            self.connection = sqlite3.connect('donthackmeplease.sqlite')
            print("Connection is established: Database is created in file")
        except Error:
            print(Error)

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE users('
                       'user_id INT AUTO_INCREMENT PRIMARY KEY,'
                       'username VARCHAR(20))')
        self.connection.commit()
