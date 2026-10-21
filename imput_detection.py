from constante import TAILLE_GRILLE, TAILLE_CASE, TAILLE_ZONE_LATERAL, TAILLE_ZONE_VERTICAL

def detection_clique(x,y):
    if y < TAILLE_CASE*TAILLE_GRILLE + TAILLE_ZONE_VERTICAL:
        return None
    x = x - TAILLE_ZONE_LATERAL
    if x < 0 or x >= TAILLE_GRILLE*TAILLE_CASE:
        return None
    return x//(TAILLE_GRILLE*TAILLE_CASE//3)

def detection_piece_lache(souris_x,souris_y):

    colonne=round((souris_x - TAILLE_ZONE_LATERAL)/TAILLE_CASE)
    ligne=round((souris_y-TAILLE_ZONE_VERTICAL)/ TAILLE_CASE)

    return colonne,ligne