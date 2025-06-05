import pygame as pg
import random

class Obstaculo:
    def __init__(self,end_imagem, la, al,pontuacao):

        self.la = la
        self.al = al
        self.pontuacao  = pontuacao
        self.imagem = pg.image.load (end_imagem)
        self.imagem = pg.transform.scale(self.imagem,(self.la,self.al))
        self.mask = pg.mask.from_surface(self.imagem)

        self.p_yi  = 0
        self.lista_pos = [100,200,300,400,500,600,700,800,900,1000]

        self.p_y =  self.p_yi
        self.p_x = random.choice(self.lista_pos)

        self.velo = (random.randint(1,6))

    def movimento(self):
        self.p_y += self.velo
        if self.p_y >= 700:
            self.p_y = self.p_yi
            self.velo = (random.randint(1,6))
            self.p_x = random.choice(self.lista_pos)
        
    def desenho (self,tela):
        tela.blit (self.imagem,(self.p_x,self.p_y))
