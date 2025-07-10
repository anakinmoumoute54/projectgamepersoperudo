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
    print("Lancement des dés...") #
    for joueur in joueurs:
        joueur["des"] = [random.randint(1, 6) for _ in joueur["des"]]

def afficher_des(joueurs): # affiche les dés des joueur
    for joueur in joueurs:
        print(f"{joueur['nom']} a les dés : {joueur['des']}")

def compter_occurrences(joueurs, valeur): # compte les valeurs des dés des joueurs
    total = 0
    for joueur in joueurs:
        total += joueur["des"].count(valeur)
    return total

def tour_de_jeu(joueurs): # gere le tour de chaque joueur
    enchere = None
    joueur_actuel = 0
    nb_joueurs = len(joueurs)

joueurs = initialisation_game()
joueur_actuel = 0
enchere = None  # Initialisation de la variable enchere
# boucle principale du jeu
while True : 
    joueur = joueurs[joueur_actuel]
    print(f"C'est le tour de {joueur['nom']}")

if enchere is None:
    # la première enchère d'un joueur
    nb = int(input("Entrez le nombre de dés pour la première enchère : "))
    valeur = int(input("Entrez la valeur du dé pour la première enchère (1-6) : "))
    enchere = (nb, valeur)
else:
    print(f"l'enchère actuelle est : {enchere[0]} dés de valeur {enchere[1]}")
    while True:
        nb = int(input("Entrez le nombre de dés pour la nouvelle enchère : "))
        valeur = int(input("Entrez la valeur du dé pour la nouvelle enchère (1-6) : "))
        if nb < enchere[0] or (nb == enchere[0] and valeur <= enchere[1]): # verification de l'enchere est valide est sup a 0
            print("Enchère invalide, elle doit être supérieure à l'enchère précédente.")
            continue
        enchere = (nb, valeur)
        break