import pygame.draw

from piece import Piece
from board import Board
from constante import *

class Renderer:
    def __init__(self,ecran):
        self.ecran= ecran
        self.police = pygame.font.Font(None, 28)
        self.police_titre = pygame.font.Font(None, 64)

    def dessiner_grille(self):

        for i in range(TAILLE_GRILLE+1):
            pygame.draw.line(self.ecran,COULEUR["noir"], (TAILLE_ZONE_LATERAL, i * TAILLE_CASE+TAILLE_ZONE_VERTICAL), (LARGEUR_FENETRE-TAILLE_ZONE_LATERAL, i * TAILLE_CASE+TAILLE_ZONE_VERTICAL))

        for j in range(TAILLE_GRILLE+1):
            pygame.draw.line(self.ecran,COULEUR["noir"], (TAILLE_ZONE_LATERAL+j * TAILLE_CASE,TAILLE_ZONE_VERTICAL), (j * TAILLE_CASE+TAILLE_ZONE_LATERAL,TAILLE_CASE*TAILLE_GRILLE+TAILLE_ZONE_VERTICAL))

    def dessiner_cellule(self,Board):

        for i in range(TAILLE_GRILLE):
            for j in range(TAILLE_GRILLE):

                 x = j * TAILLE_CASE+TAILLE_ZONE_LATERAL
                 y = i * TAILLE_CASE+TAILLE_ZONE_VERTICAL

                 if Board.board[i][j] != 0:

                     pygame.draw.rect(self.ecran,Board.board[i][j],(x,y,TAILLE_CASE,TAILLE_CASE))

    def dessiner_pieces(self,coin_x,coin_y,piece,couleur=None):
        if couleur is None:
            couleur=piece.couleur
        else:
            couleur=couleur

        for ligne in range(len(piece.forme)):
            for colonne in range(len(piece.forme[0])):
                if piece.forme[ligne][colonne] != 0:
                    x = colonne * TAILLE_CASE + coin_x
                    y = ligne * TAILLE_CASE + coin_y

                    pygame.draw.rect(self.ecran, piece.couleur, (x, y, TAILLE_CASE, TAILLE_CASE))



    def dessiner_forme_en_attente(self,Piece,index_tenu=None):



        TAILLE_X_ZONE_PIECE = (TAILLE_CASE * TAILLE_GRILLE) / 3
        CENTRE_Y_ZONE_PIECE = TAILLE_ZONE_VERTICAL+(TAILLE_GRILLE * TAILLE_CASE + TAILLE_ZONE_PIECE / 2)


        for i, piece in enumerate(Piece):
            if index_tenu ==i:
                continue
            if piece == None:
                continue
            CENTRE_X_ZONE_PIECE = TAILLE_ZONE_LATERAL+(TAILLE_X_ZONE_PIECE * i + TAILLE_X_ZONE_PIECE/2)

            coin_x = CENTRE_X_ZONE_PIECE - (len(piece.forme[0]) * TAILLE_CASE) / 2
            coin_y = CENTRE_Y_ZONE_PIECE - (len(piece.forme) * TAILLE_CASE) / 2

            self.dessiner_pieces(coin_x,coin_y,piece)

    def dessiner_score(self, score):
        texte = self.police.render(f"Score : {int(score)}", True, COULEUR["noir"])
        self.ecran.blit(texte, ((LARGEUR_FENETRE-100)/2, 20))

    def dessiner_fin_partie(self, score):
        centre_x = LARGEUR_FENETRE // 2
        centre_y = LONGEUR_FENETRE // 2

        fond = pygame.Rect(0, 0, LARGEUR_FENETRE, 200)
        fond.center = (centre_x, centre_y)
        pygame.draw.rect(self.ecran, COULEUR["noir"], fond)

        titre = self.police_titre.render("Partie terminée", True, (255, 255, 255))
        texte_score = self.police.render(f"Score : {int(score)}", True, (255, 255, 255))
        self.ecran.blit(titre, titre.get_rect(center=(centre_x, centre_y - 30)))
        self.ecran.blit(texte_score, texte_score.get_rect(center=(centre_x, centre_y + 30)))
        texte_rejouer = self.police.render("Appuie sur espace pour rejouer", True, (255, 255, 255))
        self.ecran.blit(texte_rejouer, texte_rejouer.get_rect(center=(centre_x, centre_y + 70)))