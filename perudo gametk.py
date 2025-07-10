import tkinter as tk
from tkinter import simpledialog, messagebox
import random

root = tk.Tk()
root.title("Jeu du Perudo")

joueurs = []

def initialiser_jeu():
    global joueurs
    joueurs = []

    nb_joueurs = simpledialog.askinteger("Nombre de joueurs", "Combien de joueurs ? (2-6)", minvalue=2, maxvalue=6)
    if nb_joueurs is None:
        return

    for i in range(nb_joueurs):
        nom = simpledialog.askstring("Nom du joueur", f"Nom du joueur {i + 1} :")
        if nom is None:
            nom = f"Joueur {i + 1}"
        joueurs.append({"nom": nom, "des": [1, 1, 1, 1, 1]})

    lancer_des()
    afficher_joueurs()

def lancer_des():
    for joueur in joueurs:
        joueur["des"] = [random.randint(1, 6) for _ in joueur["des"]]
    afficher_joueurs()

def afficher_joueurs():
    texte.delete(1.0, tk.END)
    for joueur in joueurs:
        texte.insert(tk.END, f"{joueur['nom']} : {joueur['des']}\n")

# boutons
bouton_init = tk.Button(root, text="Nouvelle Partie", command=initialiser_jeu)
bouton_init.pack(pady=5)

bouton_lancer = tk.Button(root, text="Lancer les dés", command=lancer_des)
bouton_lancer.pack(pady=5)

texte = tk.Text(root, width=40, height=10)
texte.pack(pady=5)

root.mainloop()
