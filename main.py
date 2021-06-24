import random
import os

print("hallo je gaat nu mastermind spelen")


kleuren = ["Rood", "Geel", "Groen", "Blauw", "Zwart", "Oranje"]

random.shuffle(kleuren)
passcode = kleuren[:4]

def mastermind():
  invoer = input("\nvoer hier je code in:")
  if invoer in passcode:
    print("Wit")

mastermind()