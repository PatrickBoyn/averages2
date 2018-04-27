"""Puts a number into the database. """
import psycopg2 as pg
 
class Connection:
    def __init__(self, db):
        self.db = db

    def db_setup(self):
        conn = pg.connect(dbname=self.db, user='postgres', host='localhost')
        cur = conn.cursor()

class AddNumber(Connection):
    add_number = "INSERT INTO {} (number_id, number, date_created) VALUES({})".format(self.db, number)