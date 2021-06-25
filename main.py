import random

def game():
  print("hallo je gaat nu mastermind spelen")
  print("Je kan kiezen uit de kleuren Rood, Groen, Blauw, Zwart en Oranje")
  print("Je moet een code invullen op deze manier: rgbz")

  kleuren = ["R", "G", "B", "Z", "O"]

  random.shuffle(kleuren)
  passcode = kleuren[:4]
  def mastermind(beurtenover):
    hints = []

    #invoer
    invoer = input("\nvoer hier je code in:").upper()
    for letter in invoer:
      if not letter in kleuren:
        print("invoer fout probeer opnieuw")
        mastermind(beurtenover)
        return
    if not invoer.isalpha() or len(invoer) != 4:
      print("invoer fout probeer opnieuw")
      mastermind(beurtenover)
      return

    #Code vergelijken met invoer en hints geven
    for i in range(4):
      letterCode = passcode[i]
      letterInvoer = invoer[i]
      # print("letter " + letterCode + " vergelijken met " +letterInvoer);
      if letterCode == letterInvoer:
        hints.append("z")
      elif letterInvoer in passcode:
        hints.append("w")
    print(hints)
    
    # checken of je wint
    if invoer == "".join(passcode):
      print("je hebt gewonnen")
      again = input("wil je nog een keer spelen? (ja/nee)")
      if again == "ja" :
        game()
      else:
        print("einde spel")
    else:
      beurtenover -= 1
      if beurtenover == 0:
        print("je hebt verloren")
        again = input("wil je nog een keer spelen? (ja/nee)")
        if again == "ja" :
          game()
        else:
          print("einde spel")
          return
      mastermind(beurtenover)
      

  mastermind(10)
game()


# nog een keer spelen
# input validatie
# eisen van de opdracht