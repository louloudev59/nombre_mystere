
# on import random
# on assigne à une variable un nombre aléatoire entre 0 et 100
# on demande à l'utilisateur à quel nombre je pense
# on vérifie si le nombre input == à la variable
# si pas bon, on le dit et on dit, il te reste plus que var vies qui est défini à 5
# par contre si nombre bon, on applaudit
import sys
from random import randint
vie = 5
nombre_mystere = randint(0, 10)
while True :
    nombre_user = int(input("Devine le nombre auquel je pense : "))
    if nombre_mystere == nombre_user:
        print("Tu es trop fort, bravo à toi !")
        sys.exit()
    elif nombre_mystere != nombre_user:
        print(f"Rahh, dommage. Attention, il ne te reste plus que {vie} vie(s)")
        vie -= 1
    if vie == -1:
            print(f"Tu as perdu, le nombre était {nombre_mystere}")
            sys.exit()
