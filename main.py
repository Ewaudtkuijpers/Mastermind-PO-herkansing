import random
import os

print("hallo je gaat nu mastermind spelen")


kleuren = ["R", "G", "B", "Z", "O"]

random.shuffle(kleuren)
passcode = kleuren[:4]
print(passcode)
def mastermind(beurtenover):
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
    beurtenover -= 1
    if beurtenover == 0:
      print("je hebt verloren")
      return
    mastermind(beurtenover)
    

mastermind(10)


# nog een keer spelen
# input validatie
# eisen van de opdracht