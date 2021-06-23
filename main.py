import random
import os

print("hallo je gaat nu mastermind spelen")
kleuren = ["Rood", "Geel", "Groen", "Blauw", "Zwart", "Oranje"]

random.shuffle(kleuren)
passcode = kleuren[:4]

input("\tvoer hier je code in:")

