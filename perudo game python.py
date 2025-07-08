# perudo.py 

import random 

def initialisation__game ():      # initialisation du jeu 
   print("===Decouvrez le jeu du Perudo===") 
   nb_joueur = int(input("Cmb de joueurs ? (2-6) : "))     # nb de joueur
   joueur = [] 
   for i in range(nb_joueur): # boucle pour joueur qui joue chacun son tour
        nom = input(f"Nom du joueur {i+1} : ")               
        joueur.append({"nom": nom, "des": [1, 1, 1, 1, 1]}) # des joués a chaque remis a 1
   return joueur

joueur = initialisation__game()
print("Jouer!")
print(joueur)

