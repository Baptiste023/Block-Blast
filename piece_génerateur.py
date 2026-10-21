import random
from piece import *
from constante import COULEUR

def selecteur_de_pièce():
    liste_pièces_choisie=[]

    for i in range(3):
        piece=random.choice(list(FORMES.keys()))
        couleur=random.choice(list(COULEUR.values()))
        piece_couleur = Piece(piece,couleur)
        liste_pièces_choisie.append(piece_couleur)
    return liste_pièces_choisie
