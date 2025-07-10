import random 

def initialisation_game():      # initialisation du game 
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
        break #fin de la boucle enchere
    
    action = input("Voulez-vous enchérir (e) ou douter (d) ? ").lower() # on dmd au joueur sil bluff ou il enchere
    if action == "d":
        # verif l'enchère
        nb_reels = compter_occurrences(joueurs, enchere[1])
        print(f"Il y a en réalité {nb_reels} dés de valeur {enchere[1]} sur la table.")
        if nb_reels >= enchere[0]:
            # Le joueur qui doute perd un dé
            print(f"{joueur['nom']} a perdu un dé.")
            if joueur["des"]:
                joueur["des"].pop()
        else:
            # Le joueur précédent perd un dé
            joueur_prec = joueurs[(joueur_actuel - 1) % len(joueurs)]
            print(f"{joueur_prec['nom']} a perdu un dé.")
            if joueur_prec["des"]:
                joueur_prec["des"].pop() # on retire un de au joueur d'avt 
        #  recommencer un tour
        lancer_des(joueurs)
        enchere = None
    else:
        while True:
            nb = int(input("Entrez le nombre de dés pour la nouvelle enchère : "))
            valeur = int(input("Entrez la valeur du dé pour la nouvelle enchère (1-6) : "))
            if nb < enchere[0] or (nb == enchere[0] and valeur <= enchere[1]):
                print("Enchère invalide, elle doit être supérieure à l'enchère précédente.")
                continue
            enchere = (nb, valeur)
            break

    # le tour est au joueur suivant
    joueur_actuel = (joueur_actuel + 1) % len(joueurs)

    # verif  si un joueur n'a plus de dés
    joueurs = [j for j in joueurs if len(j["des"]) > 0]
    if len(joueurs) == 1:
        print(f"{joueurs[0]['nom']} a gagné la partie !")
      break # fin boucle du jeu
