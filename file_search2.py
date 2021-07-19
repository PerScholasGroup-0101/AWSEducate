

print('Hello future cloud computing expert! Which of the below skills interest you the most?' )

fprint=open('skills.txt', 'r')
#this need to print a nice table for the user to select skills
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

fhand = open('descriptions.txt') #opening the txt file
#We need to be able to read multiple options input by the user
#let's search the file for the information we want
for line in fhand:
    #line = line.rstrip()
    if line.startswith(skill_path[skill]):
        print(line, end="\n")
        print(next(fhand), end="\n\n")
        #sentences = re.split(r' *[\.\?!][\'"\)\]]* *', line)
        #print(sentences)
        #(len(line))
#We need an option given to the user "do you want to learn more, and about which career pathway"        
#We may need max length function to limit the number of word(or characters printed for final output)
#We need pop-up screen for the learning pathways

