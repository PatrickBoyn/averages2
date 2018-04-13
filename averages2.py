"""This will be athe second version of my averages program. """
import psycopg2

class Averages2():
    def connection(self):
        try:
            con = psycopg2.connect("dbname='averages2' user='postgres' host='localhost'")
            cur = con.cursor()
        except:
            print("No database connected at this time. ")
        cur.close()

 
    def main(self):
        averages = input("Please enter a number, or (h)elp for help: \n")
        self.connection()

        print("This is main, am I working? The number you entered in was: " + averages)


if __name__ == "__main__":
    Averages2.main()
