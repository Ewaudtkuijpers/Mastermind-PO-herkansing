import random
import os

print("hallo je gaat nu mastermind spelen")


kleuren = ["R", "G", "B", "Z", "O"]

random.shuffle(kleuren)
passcode = kleuren[:4]
print(passcode)
def mastermind():
  hints = []

  #invoer
  invoer = input("\nvoer hier je code in:").upper()
  if not invoer.isalpha():
    print("invoer fout probeer opnieuw")
    

  #Code vergelijken met invoer en hints geven
    for i in range(4):
      letterCode = passcode[i]
      letterInvoer = invoer[i]
      print("letter " + letterCode + " vergelijken met " +letterInvoer);
      if letterCode == letterInvoer:
        hints.append("z")
      elif letterInvoer in passcode:
        hints.append("w")
    print(hints)
  
  # checken of je wint
  if invoer == "".join(passcode):
    print("je hebt gewonnen")
  else:
    mastermind()

mastermind()

# nog een keer spelen
# beurten
# input validatie
# eisen van de opdracht