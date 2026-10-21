

class Score :
    def __init__(self):
        self.score = 0
        self.niv_combo = 0
        self.dernier_score = 0

    def cal_score_forme(self, forme):
        score_forme = sum(cellule for ligne in forme for cellule in ligne )
        point_piece = score_forme *(1+0.2* self.niv_combo)
        return point_piece

    def point_suppr_ligne(self, nb_ligne, nb_colonne):
        point_suppr_ligne = (nb_ligne + nb_colonne)*20*(1+0.2*self.niv_combo)
        return point_suppr_ligne

    def cal_score (self,forme, nb_ligne, nb_colonne):
        if self.point_suppr_ligne(nb_ligne, nb_colonne):
            self.dernier_score = self.cal_score_forme(forme)+ self.point_suppr_ligne(nb_ligne, nb_colonne)
            self.niv_combo+= 1
        else:
            self.dernier_score = self.cal_score_forme(forme)

        self.score += self.dernier_score

    def reset_combo(self):
        self.niv_combo = 0
