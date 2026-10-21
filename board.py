from constante import TAILLE_GRILLE
import piece

class Board:
    def __init__(self):
        self.board = [[ 0  for i in range(TAILLE_GRILLE)] for j in range(TAILLE_GRILLE)]

    def possible_placements(self,piece,x,y):

        for i in range(len(piece.forme)):
            for j in range(len(piece.forme[i])):
                if piece.forme[i][j] == 1:

                    ligne = x + i
                    colonne = y + j

                    if ligne < 0 or ligne >= TAILLE_GRILLE or colonne < 0 or colonne >= TAILLE_GRILLE:
                        return False
                    if self.board[ligne][colonne] != 0:
                        return False
        return True

    def placer_forme(self,piece,x,y):
        if self.possible_placements(piece,x,y):
            for i in range(len(piece.forme)):
                for j in range(len(piece.forme[i])):
                    if piece.forme[i][j] == 1:
                        ligne = x + i
                        colonne = y + j
                        self.board[ligne][colonne] = piece.couleur

    def ligne_pleine(self,ligne):

      return all(case != 0 for case in self.board[ligne])

    def colonne_pleine(self, colonne):

        return all(ligne[colonne] != 0 for ligne in self.board)


    def effacer_ligne(self,ligne):

        self.board[ligne] = [0 for _ in range(TAILLE_GRILLE)]

    def effacer_colonne(self,colonne):

        for i in range(TAILLE_GRILLE):
            self.board[i][colonne] = 0

    def verification_et_suppression(self):

        ligne_suppr=[]
        colonne_suppr=[]

        for ligne in range(TAILLE_GRILLE):
            if self.ligne_pleine(ligne):
                ligne_suppr.append(ligne)

        for colonne in range(TAILLE_GRILLE):
            if self.colonne_pleine(colonne):
               colonne_suppr.append(colonne)

        for element in ligne_suppr:
            self.effacer_ligne(element)

        for element in colonne_suppr:
            self.effacer_colonne(element)

        return ligne_suppr,colonne_suppr