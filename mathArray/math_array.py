#math_array
from random import randint
from datetime import datetime
import time, sys

global count
count = 0

global start_time
start_time = datetime.now()


def time_function(time_in_seconds):
  if 3600 > time_in_seconds > 60:
    minutes = time_in_seconds // 60
    seconds = time_in_seconds % 60

    return f'{minutes:02}:{seconds:02}'

  elif time_in_seconds < 60:
    return f'0:{time_in_seconds:02}'

  elif 86400 > time_in_seconds > 3600:
    return " entirely too long!  You should consider getting a life.\n \nSeriously"

def createArray():
  global count
  rows = randint(2,10)
  columns = randint(2, 10)
  total = rows * columns
  character_fill = " o "

  print("Array #{}:\n".format(str(count + 1)))

  for i in range(0, rows):
    print(character_fill * columns, end='\n\n')

  print('\n')

  return rows, columns

def get_user_input(prompt):
  user_input = input(str(prompt))

  if user_input.isdigit():
    return int(user_input)

  elif str(user_input).lower() == "quit" or str(user_input).lower() == "exit" or str(user_input).lower() == "q" or str(user_input).lower() == "e":
    return "exit"

  elif user_input == None or user_input == "" or user_input == " ":
    return ""

  else:
    print("Please only enter whole numbers!\n")
    return None

def evaluate_user_input(user_input, expected_value, rows, columns):
  global count

  if user_input == expected_value:
    print("Good job!  You got it right!\n")
    return True

  elif user_input != expected_value and (user_input == rows or user_input == columns) and (expected_value != rows*columns):
    print("\nOops!!  It looks like you may have confused rows with columns.")
    print("Remember that rows are groups of items that run from left to right")
    print("and columns are groups of items that run up and down.\n\nTry again!\n")

  elif user_input == 'exit':
    end_time = datetime.now()
    elapsed_time = end_time - start_time

    normalized_time = time_function(int(elapsed_time.total_seconds()))

    if count > 2:
      print("\n\nWay to go!  You got {} right!!  Come back later for more practice.".format(count))
    else:
      print("\n\nYou got {} right. Come back later for more practice.".format(count))

    print("Total time = {} ".format(normalized_time))

    time.sleep(5)
    sys.exit(0)

  elif user_input == None or user_input == "":
    return None

  else:
    print("Nope, that's not right. Try again!\n")
    return False

def check_rows(rows, columns):
  rows_answer = get_user_input("How many rows are in this array? ")

  while not evaluate_user_input(rows_answer, rows, rows, columns):
    rows_answer = get_user_input("How many rows are in this array? ")

def check_columns(rows, columns):
  columns_answer = get_user_input("How many are in each row? ")

  while not evaluate_user_input(columns_answer, columns, rows, columns):
    columns_answer = get_user_input("How many are in each row? ")

def check_total(rows, columns):
  global count
  total_answer = get_user_input("How many are there in total? ")

  while not evaluate_user_input(total_answer, rows*columns, rows, columns):
    total_answer = get_user_input("How many are there in total? ")

  count += 1

def main():

  print("This program displays an array with 2-10 rows and 2-10 columns. It will")
  print("then ask you to answer how many rows there are, how many columns, and")
  print("the total of the array.\n")
  print("You will receive a prompt letting you know whether or not your answer")
  print("is correct.  This program will continue until you type 'quit' or 'exit.'")
  print("\nGood luck!!\n")

  while True:
    rows, columns = createArray()
    check_rows(rows, columns)
    check_columns(rows, columns)
    check_total(rows, columns)

    evaluate_user_input(get_user_input("Press enter to continue. To quit, type 'quit' then press enter.\n"), None, None, None)

if __name__ == '__main__':
  main()
