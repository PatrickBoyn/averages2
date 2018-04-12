"""This will be athe second version of my averages program. """
import psycopg2


AVERAGES = input("Please enter a number, or (h)elp for help: \n")

try:
    CON = psycopg2.connect("dbname='averages2' user='postgres' host='localhost'")
    CUR = CON.cursor()
except:
    print("No database connected at this time. ")
CUR.close()

def main():
    print("This is main, am I working? The number you entered in was: " + AVERAGES)


if __name__ == "main":
      main()
