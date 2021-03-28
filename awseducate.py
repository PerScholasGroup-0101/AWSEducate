# explanation of the project here

print('AWS Educate offers 12 different career pathways to continue yout IT journey')
skill_to_path = {
    'compute': 'Cloud Computing 101',
    'analytics': 'Cloud Computing 101',
    'web development': 'Application Developer', 'coding': 'Application Developer', 'scripting': 'Cloud Support Associate', 'programming': 'Cloud Support Associate', 'security': 'Cloud Support Engineer', 'network architecture': 'Cloud Support Engineer', 'network protocols': 'Cybersecurity Specialist', 'coding review': 'Cybersecurity Specialist', 'relational database': 'Data Integration Specialist',
                 'scripting in different languages': 'Data Integration Specialist', 'non-relational and relational databases': 'Data Scientist', 'programming in different languages': 'Data Scientist', 'advance coding': 'DevOps Engineer', 'one or more languages': 'DevOps Engineer', 'data analytics': 'Machine Learning Scientist', 'advance scripting': 'Machine Learning Scientist', 'advance programming and scripting languages': 'Software Development Engineer', 'data structures': 'Software Development Engineer', 'aws solutions': 'Solutions Architect', 'software development': 'Solutions Architect', 'programming and scripting': 'Web Development Engineer', 'advance data structures': 'Web Development Engineer'}
paths = []
choices = input("enter your skills: ")
for choice in choices.split():
    try:
        paths.append(skill_to_path[choice.lower()])
    except KeyError:
        print(choice, "is not a valid skill")

print("Your paths are:", ', '.join(paths))
