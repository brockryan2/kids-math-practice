# math_multiplication_quiz
from random import randint
import sys, time


def multiplicationQuiz(number_of_questions=2, difficulty='easy'):

  operator_limit = 9
  number_correct = 0

  if difficulty == 'medium':
    operator_limit = 12

  if difficulty == 'hard':
    operator_limit = 20

  for question in range(1, number_of_questions + 1):

    a = randint(1, operator_limit)
    b = randint(1, operator_limit)

    print("Question {}: What is {} x {}".format(question, a, b))

    answer = int(input())

    while answer != a * b:
      print("Sorry, that's not right. Try again")

      print("What is {} x {}".format(a, b))

      answer = int(input())

    print("Great job!")


""" code block for scoring --> remove while block for retries before enabling this block

    number_correct += 1

  percentage_correct = (number_correct / number_of_questions) * 100.0
  results = ""

  if percentage_correct > 85.0:
    results = "Great job! You got {} out of {} right. Score: {}%".format(number_correct, number_of_questions, percentage_correct)

  elif percentage_correct > 60.0:
    results = "Not bad. You got {} out of {} right. Score: {}%\nKeep practicing!".format(number_correct, number_of_questions, percentage_correct)

  else:
    results = "Uh oh. You only got {} out of {} right. Score: {}%\nTry harder next time.".format(number_correct, number_of_questions, percentage_correct)

  print(results)
"""

def main():

  print("Welcome! This is a simple multiplication quiz game to help you get better at multiplication.\n \n ")

  time.sleep(2)

  multiplicationQuiz()

  print("\nWant to try again?")
  try_again = input()

  try_again = try_again.lower()

  try_again == 'y':
    multiplicationQuiz()

  else:
    print("Come back again soon!")
    time.sleep(1)
    print("Closing program", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".", end="")
    sys.exit(0)

if __name__ == '__main__':
  main()
