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
skill_int = (skill_path[skill])
print(skill_int)
