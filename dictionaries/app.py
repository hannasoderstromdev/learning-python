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


def add_mark_to_student(student, number):
  student['marks'].append(number)

def calc_avg_mark(student):
  number = len(student['marks'])
  if number == 0:
    return 0

  total = sum(student['marks'])
  return total / number

student = create_student()
add_mark_to_student(student, 1)
add_mark_to_student(student, 1)
add_mark_to_student(student, 1)

print(calc_avg_mark(student))