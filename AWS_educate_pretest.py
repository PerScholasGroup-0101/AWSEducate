import tkinter #importing module for creating the popup text box at the end
from tkinter import messagebox
from tkinter import simpledialog

print("Hello everyone!\nWelcome to AWS Educate Program.") #The simplest of python commands
name = input("what is your name? ")
print("Hello!", name)
print('\n future cloud computing expert! Which of the below skills interest you the most?')
print('+---------------------------------------------++---------------------------------------------+\n| Num |                Skills                 |  Num |                Skills                 |\n+---------------------------------------------++---------------------------------------------+\n|  1  | Compute- storage- analytics           |  7   | RDB and non RDB-programming languages |')
print('+---------------------------------------------++---------------------------------------------+\n|  2  | Web development-Coding-programming    |  8   | Coding-scripting languages            |\n+---------------------------------------------++---------------------------------------------+\n|  3  | Scripting- Programming language       |  9   | Distributed systems- Data Analytics   |')
print('+---------------------------------------------++---------------------------------------------+\n|  4  | Network Architecture- security        |  10  | Programming-scripting-data            |\n+---------------------------------------------++---------------------------------------------+\n|  5  | Network Protocols- Coding             |  11  | AWS solutions-network architecture    |')
print('+---------------------------------------------++---------------------------------------------+\n|  6  | RDB - scripting languages             |  12  | Programming-scripting languages       |\n+---------------------------------------------++---------------------------------------------+\n')
#creating a dictionary
skill_path = {'1': 'Cloud Computing 101',
              '2': 'Application Developer',
              '3': 'Cloud Support Associate',
              '4': 'Cloud Support Engineer',
              '5': 'Cybersecurity Specialist',
              '6': 'Data Integration Specialist',
              '7': 'Data Scientist',
              '8': 'DevOps Engineer',
              '9': 'Machine Learning Scientist',
              '10': 'Software Development Engineer',
              '11': 'Solutions Architect',
              '12': 'Web Development Engineer'
              }
#creating a list
paths = []
choices = input(
    "choose corresponding numbers for up to 3 skills/interests, separated by spaces: ")
for choice in choices.split():
    try:
        paths.append(skill_path[choice]) #adding to the paths list created earlier
    except KeyError: #don't forget to account for user error
        print(choice, "is not a valid entry ")

length=int(len(paths)) #how many characters or items long is the list we created? We want to know how many entries the user made.
interest_list=0 #new variable created here for counting during the while loop we've created below
list_number=1 #remember that when Python assigns index numbers to items in a list, it starts at zero. the list we create for our user will start at 1

while interest_list <= length: #we will run the loop the number of times that the list is long
    try:
        print(list_number,".",paths[interest_list])
        interest_list += 1 #every time we run the loop we'll count
        list_number += 1 #remember this number starts at 1, this is the user's numbered list
    except IndexError: #just in case the user enters an invalid number
        break
    
print()
tanz = input('Would you like to learn more? (y/n) ')   #no reason at all we named that variable 
for tanz1 in tanz: #another loop that we use to check for errors in user input
    if tanz == 'y':
        lyda = input('Please enter the number of the corresponding career pathway that you would like to learn more about:')
        if int(lyda) > length: 
            print("Invalid option. It can not be greater than", length)
            break
        skills=(paths[(int(lyda)-1)])
        fhand = open('descriptions.txt')  # opening the txt file
        for line in fhand:
            if line.startswith(skills): 
                line1 = line
                def printout(): #creating a function
                    messagebox.showinfo("AWS Career Paths", line1)
    
                root = tkinter.Tk()
                root.withdraw()

                printout()
                
    elif tanz == 'n':
       break
    else:
        print("input not valid")

