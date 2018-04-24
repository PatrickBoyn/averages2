"""This will be athe second version of my averages program. """
import psycopg2
from datetime import datetime
class Averages:

    def connection(self):
        start = datetime.now()
        try:
            conn = psycopg2.connect("dbname='averages2' user='postgres' host='localhost'")
            cur = conn.cursor()
        except psycopg2.OperationalError:
             print("No database by that name exists. ")
        end = datetime.now()
        final = end - start
        print("The program took: " + str(final))

A = Averages()

A.connection()
