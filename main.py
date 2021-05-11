import sys
import random
from art import logo

print(logo)


number = random.randint(1, 100)

user_guessed = False

LIVES = 0

print("The two game modes are Easy mode and Hard mode.\nEasy mode gives you 10 attempts" + " to get the answer correct.\nHard mode only gives you 5 attempts.\n")


def select_difficulty():
  game_mode = input("Pick a gamemode: \nEasy\nHard\n\n")
  return game_mode

game_mode = select_difficulty()

def guess_a_number(guess, correct_number, LIVES, game_mode):
  answer = int(input("\nGuess a number between 1-100\n"))
  if answer == correct_number:
    guess = True
    print("You've guessed correctly!")
    sys.exit("Good job")
  elif answer < correct_number and game_mode == 'easy' and LIVES < 10:
    print("\nGuess a higher number next time")
  elif answer < correct_number and game_mode == 'hard' and LIVES < 5:
    print("\nGuess a higher number next time")
  elif answer > correct_number and game_mode == 'easy' and LIVES < 10:
    print("\nGuess a lower number next time")
  elif answer > correct_number and game_mode == 'hard' and LIVES < 5:
    print("\nGuess a lower number next time")
    

while user_guessed == False and game_mode == "easy":
  LIVES += 1
  if LIVES <= 10:
    guess_a_number(user_guessed, number, LIVES, game_mode) 
  else:
    print("You're out of LIVES.")
    print(f"The correct number was {number}")
    sys.exit("Better luck next time!")

while user_guessed == False and game_mode == "hard":
  LIVES += 1
  if LIVES <= 5:
    guess_a_number(user_guessed, number, LIVES, game_mode) 
  else:
    print("\nYou're out of LIVES.")
    print(f"The correct number was {number}")
    sys.exit("Better luck next time!")