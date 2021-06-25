import random
import os

print("hallo je gaat nu mastermind spelen")


kleuren = ["R", "G", "B", "Z", "O"]

random.shuffle(kleuren)
passcode = kleuren[:4]
print(passcode)
def mastermind():
  invoer = input("\nvoer hier je code in:")
  for i in range(4):
    letterCode = passcode[i]
    letterInvoer = invoer[i]
    print("letter " + letterCode + " vergelijken met " +letterInvoer);
    if letterCode == letterInvoer:
      print("letter op goede plek")
    elif letterInvoer in passcode:
      print("letter op de verkeerde plek")
    else:
      print("letter zit er niet in")
    # if letter in passcode:
    #   print(letter + " zit erin")
    # else:
    #   print(letter + " zit er niet in")
  

mastermind()