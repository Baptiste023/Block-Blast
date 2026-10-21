from board import Board
from score import Score
from piece_génerateur import selecteur_de_pièce
from constante import TAILLE_GRILLE


class Game:
    def __init__(self):
        self.plateau = Board()
        self.pieces = selecteur_de_pièce()
        self.score = Score()
        self.suppr_avec_3_derniere_forme= False
        self.fin=False

    def jouer_pieces(self,index,ligne,colonne):
        piece=self.pieces[index]
        if self.plateau.possible_placements(piece,ligne,colonne):
            self.plateau.placer_forme(piece,ligne,colonne)
            ligne_suppr,colonne_suppr=self.plateau.verification_et_suppression()
            self.score.cal_score(piece.forme, len(ligne_suppr), len(colonne_suppr))
            if len(ligne_suppr) or len(colonne_suppr):
                self.suppr_avec_3_derniere_forme = True
            self.pieces[index] = None
            verif=all(piece is None for piece in self.pieces)

            if verif:
                self.pieces=selecteur_de_pièce()
                if not self.suppr_avec_3_derniere_forme:
                    self.score.reset_combo()
                self.suppr_avec_3_derniere_forme= False
            self.fin=self.partie_terminee()
            return True
        else:
            return False

    def partie_terminee(self):
        for piece in self.pieces:
            if piece is None:
                continue
            for ligne in range(TAILLE_GRILLE):
                for colonne in range(TAILLE_GRILLE):
                    if self.plateau.possible_placements(piece, ligne, colonne):
                        return False
        return True