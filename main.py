import random
import os

print("hallo je gaat nu mastermind spelen")


kleuren = ["R", "G", "B", "Z", "O"]

random.shuffle(kleuren)
passcode = kleuren[:4]
print(passcode)
def mastermind():
  invoer = input("\nvoer hier je code in:")
  for letter in invoer:
    if letter in passcode:
      print(letter + " zit erin")
    else:
      print(letter + " zit er niet in")
  

mastermind()