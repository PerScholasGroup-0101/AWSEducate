#needed near beginning!
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
print("Hello everyone !")
print("Welcome to AWS Eduacate Program.")
name = input("what is your name ?")
print("Hello!", name)

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

#print("Your paths are:", ', '.join(paths))
#print(len(paths))
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
tanz = input('Would you like to learn more? (y/n)')   #no reason at all we named that variable 
if tanz == 'y':
    lyda = input('Please enter the number of the corresponding career pathway that you would like to learn more about:')
#lyda = int(lyda)
skills=(paths[(int(lyda)-1)])

fhand = open('descriptions.txt')  # opening the txt file
#We need to be able to read multiple options input by the user
#let's search the file for the information we want
#def output():
for line in fhand:
    line = line.rstrip()
    if line.startswith(skills):
        print(line, end="\n")
        print(next(fhand), end="\n\n")

root = tkinter.Tk()
root.withdraw()
#literally place holder for output

#def printout():
#    messagebox.showinfo("AWS Career Paths", output())

#printout()
    
    
