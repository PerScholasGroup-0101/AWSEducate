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
    print(list_number,".",paths[interest_list])
    interest_list += 1
    list_number += 1
 
