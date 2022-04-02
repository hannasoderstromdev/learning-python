import random

# Get users guesses
def get_player_numbers():
  number_csv = input("Enter 6 numbers, separated by commas: ")
  number_list = number_csv.split(",")
  integer_set = { int(number) for number in number_list }
  return integer_set

# Generate 6 random numbers (between 1-10)
def create_lottery_numbers(): 
  values = set()
  
  while len(values) < 6:
    values.add(random.randint(1,10))
  
  return values

# Match user and lottery numbers



# Calculate winnings based on numbers matched

print(create_lottery_numbers())