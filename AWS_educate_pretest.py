import tkinter
from tkinter import messagebox
from tkinter import simpledialog

print("Hello everyone!\nWelcome to AWS Educate Program.")
name = input("what is your name? ")
print("Hello!", name)
print('\n future cloud computing expert! Which of the below skills interest you the most?')
#print("\033[1;34;40m")
print('+---------------------------------------------++---------------------------------------------+\n| Num |                Skills                 |  Num |                Skills                 |\n+---------------------------------------------++---------------------------------------------+\n|  1  | Compute- storage- analytics           |  7   | RDB and non RDB-programming languages |')
print('+---------------------------------------------++---------------------------------------------+\n|  2  | Web development-Coding-programming    |  8   | Coding-scripting languages            |\n+---------------------------------------------++---------------------------------------------+\n|  3  | Scripting- Programming language       |  9   | Distributed systems- Data Analytics   |')
print('+---------------------------------------------++---------------------------------------------+\n|  4  | Network Architecture- security        |  10  | Programming-scripting-data            |\n+---------------------------------------------++---------------------------------------------+\n|  5  | Network Protocols- Coding             |  11  | AWS solutions-network architecture    |')
print('+---------------------------------------------++---------------------------------------------+\n|  6  | RDB - scripting languages             |  12  | Programming-scripting languages       |\n+---------------------------------------------++---------------------------------------------+\n')

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

paths = []
choices = input(
    "choose corresponding numbers for up to 3 skills/interests, separated by spaces: ")
for choice in choices.split():
    try:
        paths.append(skill_path[choice])
    except KeyError:
        print(choice, "is not a valid entry ")

length=int(len(paths))
interest_list=0
list_number=1

while interest_list <= length:
    try:
        print(list_number,".",paths[interest_list])
        interest_list += 1
        list_number += 1
    except IndexError:
        break
    
print()
tanz = input('Would you like to learn more? (y/n) ')   #no reason at all we named that variable 
for tanz1 in tanz:
    if tanz == 'y':
        lyda = input('Please enter the number of the corresponding career pathway that you would like to learn more about:')
#lyda = int(lyda)
        if int(lyda) > length:
            print("Invalid option. It can not be greater than", length)
            break
        skills=(paths[(int(lyda)-1)])
        fhand = open('descriptions.txt')  # opening the txt file
        for line in fhand:
            if line.startswith(skills):
                line1 = line
                def printout():
                    messagebox.showinfo("AWS Career Paths", line1)
    
                root = tkinter.Tk()
                root.withdraw()

                printout()
                
    elif tanz == 'n':
       break
    else:
        print("input not valid")

