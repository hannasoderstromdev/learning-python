import random

def menu():
  # Get users guesses
  user_numbers = get_player_numbers()

  # Generate 6 random numbers (between 1-10)
  lottery_numbers = create_lottery_numbers()

  # Match user and lottery numbers
  matched_numbers = user_numbers.intersection(lottery_numbers)
  # Print winnings
  print("You matched {}. You won €{}".format(matched_numbers, 10 ** len(matched_numbers)))
  
def get_player_numbers():
  number_csv = input("Enter 6 numbers, separated by commas: ")
  number_list = number_csv.split(",")
  integer_set = { int(number) for number in number_list }
  return integer_set

def create_lottery_numbers(): 
  values = set()
  
  while len(values) < 6:
    values.add(random.randint(1,10))
  
  return values


menu()