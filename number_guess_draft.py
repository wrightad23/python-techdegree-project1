#This is my guessing game

#This is how I do it with a function
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
#    again = input("Would you like to play again? yes/no: ")
#    if again.lower() == "yes":
#      print("I'm so sorry, I thought I was ready to handle this. Alas, I am not. Good luck though!")
#      break
#    else:
#      print("Thank you for playing!")
#      break


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

"""
#This is how I do it by boilerplate
print("Welcome to the Guessing-est Guess Game of them all!\nWe are going to play a little game where you - the player - try to guess the exact number we are thinking of!\nGood luck!")
import random
import time
print("We are now thinking of a number...")
gen_number = randrange(1, 11)  #randomly generated number
time.sleep(3)
print("Ok! Got it! Now it's your turn!")
guess_number = input("What is your guess? ")
x = 0

while True:
  x += 1
  if guess_number < gen_number:
    print("Ouch! That's too low! Keep guessin'!")
    number = input("What is your new guess? ")
    continue
  elif guess_number > gen_number:
    print("Wowza! That's too high! Keep guessin'!")
    number = input("What is your new guess? ")
    continue
  elif number == gen_number:
    print("You did it! You beat the computer! Skynet is not a threat...yet!")
    again = input("Would you like to play again? yes/no: ")
"""