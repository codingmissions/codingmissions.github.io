import random

actual_num = random.randint(1, 100)

num_of_guesses = 0

name = input("Hey, may I know your first name? ")
name = name.capitalize() # Make the first letter capital

while num_of_guesses < 10:
  guess_num = input("Guess a number from 1 to 100: ")
  guess_num = int(guess_num)
  # input(...) above return string, hence we need to convert to integer

  num_of_guesses = num_of_guesses + 1
  # you can write above as num_of_guesses += 1
  guesses_left = 10 - num_of_guesses

  if guess_num < actual_num:
    guesses_left = str(guesses_left)
    print(name + ", your guess was low, please enter a higher number. You have " + guesses_left + " guesses left")

  if guess_num > actual_num:
    guesses_left = str(guesses_left)
    print(name + ", your guess was high, please enter a lower number. You have " + guesses_left + " guesses left")

  if guess_num == actual_num:
    break

if guess_num == actual_num:
  num_of_guesses = str(num_of_guesses)
  print("Good job, " + name + "! You guessed the number in " + num_of_guesses + " tries :) .")

if guess_num != actual_num:
  actual_num = str(actual_num)
  print("Sorry " + name + ". The number I was thinking of was " + actual_num + " :)")

