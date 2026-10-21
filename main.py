import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP

from constante import*
from game import Game
from renderer import Renderer
from imput_detection import *

pygame.init()
ecran=pygame.display.set_mode((LARGEUR_FENETRE,LONGEUR_FENETRE))
pygame.display.set_caption("Bloc Blast")
clock = pygame.time.Clock()
piece_tenu,colonne,ligne=None,None,None
dessin_plateau = Renderer(ecran)
jeu=Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == MOUSEBUTTONDOWN:
           if not jeu.fin:
               x, y = event.pos[0], event.pos[1]
               piece_tenu = detection_clique(x, y)
               if piece_tenu is not None and jeu.pieces[piece_tenu] is None:
                   piece_tenu = None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and jeu.fin:
                jeu = Game()
                piece_tenu = None

        if event.type == MOUSEBUTTONUP:
            if piece_tenu is not None:
                jeu.jouer_pieces(piece_tenu,ligne,colonne)
                piece_tenu = None

    ecran.fill((255,255,255))
    dessin_plateau.dessiner_grille()
    dessin_plateau.dessiner_cellule(jeu.plateau)
    dessin_plateau.dessiner_forme_en_attente(jeu.pieces, piece_tenu)
    dessin_plateau.dessiner_score(jeu.score.score)
    if jeu.fin:
        dessin_plateau.dessiner_fin_partie(jeu.score.score)
    if piece_tenu is not None:

        souris_x, souris_y = pygame.mouse.get_pos()
        piece = jeu.pieces[piece_tenu]
        coin_x = souris_x - len(piece.forme[0]) * TAILLE_CASE / 2
        coin_y = souris_y - len(piece.forme) * TAILLE_CASE / 2
        colonne, ligne = detection_piece_lache(coin_x, coin_y)

        if jeu.plateau.possible_placements(piece, ligne, colonne):
            pixel = TAILLE_ZONE_LATERAL + colonne * TAILLE_CASE, TAILLE_ZONE_VERTICAL + ligne * TAILLE_CASE
            dessin_plateau.dessiner_pieces(pixel[0], pixel[1], piece)
        else:
            dessin_plateau.dessiner_forme_en_attente(jeu.pieces, piece_tenu)
            dessin_plateau.dessiner_pieces(coin_x, coin_y, piece)


    pygame.display.flip()
    clock.tick(FPS)

