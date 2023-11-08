#Import the json class library 
import json


#Create the data dictionary

data = {
    'name': 'Jester Molina',
    'age': 26,
    'city': 'Auburn, WA',
    'interests': ['Dancing','Video Games','Music'],
    'is_student': True
}

#With statement
with open('data.json','w') as json_file:
    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')