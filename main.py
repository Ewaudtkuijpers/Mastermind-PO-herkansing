import random
import os

print("hallo je gaat nu mastermind spelen")


kleuren = ["R", "G", "B", "Z", "O"]
hints = []

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
      hints.append("z")
    elif letterInvoer in passcode:
      hints.append("w")
  print(hints)
mastermind()