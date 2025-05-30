import pygame as pg
import random

class Obstaculo:
    def __init__(self,end_imagem, la, al):

        self.la = la
        self.al = al
        self.imagem = pg.image.load (end_imagem)
        self.imagem = pg.transform.scale(self.imagem,(self.la,self.al))

        self.p_yi  = 0
        self.lista_pos = [200,300,400,500,600,700,800,900,1000]

        self.p_y =  self.p_yi
        self.p_x = random.choice(self.lista_pos)

        self.velo = (random.randint(3,6))
