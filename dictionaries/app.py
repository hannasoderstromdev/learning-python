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

def student_details(student):
  print("{}, average mark: {}".format(student['name'], calc_avg_mark(student)))

def print_students_details(student_list):
  for i, student in enumerate(student_list):
    print("ID: {}".format(i))
    student_details(student)

def menu():
  selection = input("Enter 'p' to print the student list, "
              "'a' to add a new student, "
              "'m' to add mark to a student, "
              "or 'q' to quit."
              "Enter your selection: ")

  student_list = []
  
  while selection != 'q':
    if selection == 'p':
      print_students_details(student_list)
    
    elif selection == 'a':
      student_list.append(create_student())
    
    elif selection == 'm':
      student_id = int(input("Enter student ID: "))
      student = student_list[student_id]
      new_mark = int(input("Enter mark: "))
      add_mark_to_student(student, new_mark)

    selection = input("Enter 'p' to print the student list, "
                  "'a' to add a new student, "
                  "'m' to add mark to a student, "
                  "or 'q' to quit."
                  "Enter your selection: ")
  
  print("Bye!")

menu()