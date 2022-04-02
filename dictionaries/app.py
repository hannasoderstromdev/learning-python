# Dictionary: key-value pairs
sample_dictionary = {
  "name": "Hanna", 
  "age": 38, 
  "pets": ["Xena", "Atlas", "Zeus"], 
  "numbers": [1, 2, 3, 4], 
  "spouse": { 
    "Issy": { "age": 35 } 
  } 
}

#print(sample_dictionary)

def create_student():
  name = input("Enter the student's name: ")

  student = { 'name': name, 'marks': [] }

  return student


print(create_student())