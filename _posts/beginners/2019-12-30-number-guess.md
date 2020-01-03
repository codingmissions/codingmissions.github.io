---
date: 2019-12-30
title: Number Guess Game
description: |
  Build a number guessing game where MissionBot will choose any random number between
  1 to 100.
description_steps:
  - If the user failed to enter the random number, the user will get a hint from MissionBot in the form of "Your guess was low, please enter higher number." if number is lower than the random number and vice-versa.
  - Print message "Hurray! You Won."
  - Also, calculate the score.
index: 1
categories:
  - beginners
type: Mission
---

## Welcome Soldier!

`COMMAND:` Understand the description carefully. Gather the tools and gain the knowledge.
And, follow the steps to complete. At the end, you will know what you have achieved gradually.
`Good Luck!` :thumbsup: `See you at the end of page.` 

## Mission Description

Build a number guessing game where `MissionBot` will choose any random number between 1 to 100.
Then, ask the user to guess the correct number. Maximum allowed guessing is 10.

If the user failed to enter the correct number then display the hints as following:
- `Your guess was low, please enter a higher number` when guessed number is less than correct number.
- `Your guess was high, please enter a lower number` when guessed number is greater than correct number.

## Tools & Knowledge Required

  - Gather your Enthusiasm and Passion to Learn
  - Required basic knowledge of Python `Variables`, `Loop`, `Conditional Operators` and `Getting input from User`
  - Gain Implementation Knowledge:
    {% include image.html img="beginners/number-guess.jpg" %}

## Steps to complete Mission

Hope you have properly gained the Tools and Implementation knowledge.

Follow the steps below to complete your mission.
- Before even asking user, let's generate a random number `actual_num`.
  ```python
  import random

  actual_num = random.randomint(1, 100)
  ```
- Let's create a variable to track number of guess we made to find the correct answer.
  ```python
  num_of_guesses = 0
  ```
- Let's ask user his or her name.
  ```python
  name = input("Hey, may I know your first name? ")
  name = name.capitalize() # Make the first letter capital
  ```
- Until the number of guess is less than maximum allowed guess i.e `10`, repeat guessing number, 
  compare it with actual number and print the hint accordingly. If you found guess number is equal 
  to actual number then break out of loop.
  ```python
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
  ```
- Now, print the final message and number of guess taken.
  ```python
  if guess_num == actual_num:
    num_of_guesses = str(num_of_guesses)
    print("Good job, " + name + "! You guessed the number in " + num_of_guesses + " tries :) .")

  if guess_num != actual_num:
    actual_num = str(actual_num)
    print("Sorry " + name + ". The number I was thinking of was " + actual_num + " :)")
  ```  

## Execution Demo

```bash
Hey, may I know your first name? brg
Guess a number from 1 to 100: 50
Brg, your guess was low, please enter a higher number. You have 9 guesses left
Guess a number from 1 to 100: 70
Brg, your guess was low, please enter a higher number. You have 8 guesses left
Guess a number from 1 to 100: 90
Brg, your guess was high, please enter a lower number. You have 7 guesses left
Guess a number from 1 to 100: 80
Brg, your guess was high, please enter a lower number. You have 6 guesses left
Guess a number from 1 to 100: 75
Brg, your guess was high, please enter a lower number. You have 5 guesses left
Guess a number from 1 to 100: 72
Brg, your guess was low, please enter a higher number. You have 4 guesses left
Guess a number from 1 to 100: 73
Good job, Brg! You guessed the number in 7 tries :) .
```
