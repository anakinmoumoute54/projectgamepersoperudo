import random 

def initialisation_game():      # initialisation du jeu 
    print("=== Découvrez le jeu du Perudo ===") 
    nb_joueur = int(input("Combien de joueurs ? (2-6) : "))     # nb de joueurs
    joueur = [] 
    for i in range(nb_joueur):  # boucle pour chaque joueur
        nom = input(f"Nom du joueur {i+1} : ")               
        joueur.append({"nom": nom, "des": [1, 1, 1, 1, 1]})  # dés initialisés à 1
    return joueur

def lancer_des(joueurs):  # lance les dés pour chaque joueur
    print("Lancement des dés...") 
    for joueur in joueurs:
        joueur["des"] = [random.randint(1, 6) for _ in joueur["des"]]

def afficher_des(joueurs):
    for joueur in joueurs:
        print(f"{joueur['nom']} a les dés : {joueur['des']}")