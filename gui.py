# !C:\Users\dakil\Python3.6.5

import tkinter
import sys
mainWindow = tkinter.Tk()

mainWindow.title("Averages")
mainWindow.geometry("472x200")

label = tkinter.Label(mainWindow, 
text="Enter numbers into the database, or click one of the button to find out info.")
label.grid(column=1, row=0)
leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

enter = tkinter.Button(leftFrame, text="Enter number")
enter.grid(column=1, row=1)
averages = tkinter.Button(leftFrame, text="Get Averages")
averages.grid(column=2,row=1)
difference = tkinter.Button(leftFrame, text="Difference of two most recent")
difference.grid(column=3, row=1)
tops = tkinter.Button(leftFrame, text="Min and max differences")
tops.grid(column=4, row=1)
label2 = tkinter.Label(mainWindow, text=sys.version)
label2.grid(column=1, row=4)
data = tkinter.Entry(leftFrame)
data.grid(column=1,row=2, rowspan="2")

mainWindow.mainloop()
