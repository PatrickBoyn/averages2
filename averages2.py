"""This will be athe second version of my averages program. """
import psycopg2


AVERAGES = input("Please enter a number, or (h)elp for help: \n")

try:
    CON = psycopg2.connect("dbname='' user='postgres' host='localhost'")
    CUR = CON.cur()
except:
    print("No database connected at this time. ")

def main():
    print("This is main, am I working? The number you entered in was: " + AVERAGES)


if __name__ == "main":
    main()
