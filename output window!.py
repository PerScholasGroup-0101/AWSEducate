
#needed near beginning!
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
root = tkinter.Tk()
root.withdraw()
#literally place holder for output
l = "Placeholder"
def printout():
    messagebox.showinfo("AWS Career Paths", l)
#Natalia I put this in here to see if you can work with your table.
#l = simpledialog.askstring(title="AWS",
#                                  prompt="What subject do you wish to learn?\n"
#                                 "1- Compute-storage-analytics\n"
#                                  "2- Web development-Coding-prgramming\n"
#                                  "3- Scripting-Programming language\n" 
#                                  "4- Network Architecture-security\n" 
#                                  "5- Network Protocols-Coding\n" 
#                                  "6- Relational databases-scripting languages\n" 
#                                  "7- Relational & non-relational databases-programming languages\n"
#                                  "8- Coding-scripting languages\n"
#                                  "9- Distributed systems-Data Analytics\n"
#                                  "10- Programming-scripting-data\n"
#                                  "11- AWS solutions-network architecture\n"
#                                  "12- Programming-scripting languages\n"
#                                  )

#print("Thanks for selecting", l)

printout()