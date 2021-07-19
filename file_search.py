print('Hello future cloud computing expert! Which of the below skills interest you the most?' )

fprint=open('skills.txt', 'r')

print(fprint.read())

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

skill = input('What skill 1-12 are you most interested in? ')

skill_int=str(skill_path[skill])

print(skill_int)

fhand = open('descriptions.txt') #opening the txt file
#import re #importing regular expressions
#print(fhand.read()) # this will print the file being called by fhand

#let's search the file for the information we want
for line in fhand:
    #line = line.rstrip()
    if line.startswith(skill_int):
        print(line, end="\n")
        print(next(fhand), end="\n")
        #sentences = re.split(r' *[\.\?!][\'"\)\]]* *', line)
        #print(sentences)
        #(len(line))
        
