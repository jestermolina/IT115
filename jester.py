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

#With statement to read the data from a JSON file
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

#Print statement that confirms data has been written
print('Data has been written to data.json')



#Reading data from a JSON file using a with statement
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.sjon")
print(loaded_data)

#Read the data from the dictionary 
loaded_data['age'] = 27
#Append into the interest array 
loaded_data['interests'].append('Concerts')

#Pass in the data object and the argument to write over it
with open('data.json', 'w') as json_file:

    json.dump(loaded_data, json_file, indent=4)

print('Modified data written to data.json')

