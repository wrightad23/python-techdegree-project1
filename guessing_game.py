#This is my guessing game

def guess(guess_number):
  low_guess = "Ouch! That's too low! Keep guessin'!"
  high_guess = "Wowza! That's too high! Keep guessin'!"
  new_guess = "What is your new guess? 1-10: "
  error_message = "You did not enter a number! Please try again!"
  win_msg = "You did it! You beat the computer! Skynet is not a threat...yet!"
  single_attempt = "It only took you a single try to get it right!"
  x = 0
  while True:
    if guess_number < gen_number:
      x += 1
      print(low_guess)
      er = True
      while er == True:
        guess_number = input(new_guess)
        try:
          guess_number = int(guess_number)
          er = False
        except:
          print(error_message)
          continue
    elif guess_number > gen_number:
      x += 1
      print(high_guess)
      er = True
      while er == True:
        guess_number = input(new_guess)
        try:
          guess_number = int(guess_number)
          er = False
        except:
          print(error_message)
          continue
    elif guess_number == gen_number:
      x += 1
      print(win_msg)
      if x == 1:
        print(single_attempt)
      else:
        many_attempts = "It took you {} tries to guess correctly! Try to beat your high score!".format(x)
        print(many_attempts)
        break


import random
import time
er = True
print("Welcome to the Guessing-est Guess Game of them all!\nWe are going to play a little game where you - the player - try to guess the exact number we are thinking of!\nGood luck!")
print("We are now thinking of a number from 1 to 10...")
gen_number = random.randrange(1, 11)
time.sleep(3)
print("Ok! Got it! Now it's your turn!")
while er == True:
  guess_number = input("What is your guess? ")
  try:
    guess_number = int(guess_number)
    er = False
  except:
    print("You did not enter a number! Please try again!")
    continue
guess(guess_number)