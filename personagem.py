import pygame as pg

class Morgana:
    def __init__(self,end_imagem, l, a, xi, yi): #Define o personagem com todos os parâmetros definidos de uma só vez.
        self.imagem = pg.image.load (end_imagem)
        self.imagem = pg.transform.scale(self.imagem,(l,a))
        self.masc = pg.mask.from_surface(self.imagem)

        self.p_x = xi
        self.p_y = yi

        self.la = l
        self.al = a

    def moviment(self,t_d,t_e):
        t = pg.key.get_pressed()
        if t [t_d] and self.p_x <= 1200-self.la:
            self.p_x += 7
        elif t [t_e] and self.p_x >= 0:
            self.p_x -= 7
