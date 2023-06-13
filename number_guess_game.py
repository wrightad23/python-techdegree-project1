#This is my guessing game

def guess(guess_number):
  x = 0
  while True:
    if guess_number < gen_number:
      x += 1
      print("Ouch! That's too low! Keep guessin'!")
      guess_number = input("What is your new guess? ")
      guess_number = int(guess_number)
      continue
    elif guess_number > gen_number:
      x += 1
      print("Wowza! That's too high! Keep guessin'!")
      guess_number = input("What is your new guess? ")
      guess_number = int(guess_number)
      continue
    elif guess_number == gen_number:
      x += 1
      print("You did it! You beat the computer! Skynet is not a threat...yet!")
      if x == 1:
        print("It only took you a single try to get it right!")
      else:
        print("It took you {} tries to guess correctly! Try to be your high score!".format(x))


import random
import time
print("Welcome to the Guessing-est Guess Game of them all!\nWe are going to play a little game where you - the player - try to guess the exact number we are thinking of!\nGood luck!")
print("We are now thinking of a number from 1 to 10...")
gen_number = random.randrange(1, 11)  #randomly generated number
time.sleep(3)
print("Ok! Got it! Now it's your turn!")
guess_number = input("What is your guess? ")
guess_number = int(guess_number)
guess(guess_number)