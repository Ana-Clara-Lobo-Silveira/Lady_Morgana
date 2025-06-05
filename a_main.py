import pygame as pg
import random
from personagem import Morgana
from obstaculos import Obstaculo

pg.init() #Configurações iniciais
r = pg.time.Clock()
pontuacao = 0
tela = pg.display.set_mode((1200,800)) #Criando tela
pg.display.set_caption("Lady Morgana") #Nome do jogo


morgana = Morgana("imagem/morgana__.png",120,208,550,550)

fundo = pg.image.load ("imagem/cenario_02.png") #Decidindo o cenário
tela.blit (fundo,(0,0)) #Desenhando o cenário
o = [Obstaculo("imagem/pocao_a.png",70,70,10), #Lista de obstáculos
     Obstaculo("imagem/vinho.png",70,70,2),
     Obstaculo("imagem/morcego.png",80,80,1),
     Obstaculo("imagem/bolsa.png",70,70,6),
     Obstaculo("imagem/sangue.png",70,70,3),
     Obstaculo("imagem/grimorio.png",60,70,2),
     Obstaculo("imagem/pocao_m.png",70,70,-1000),
     Obstaculo("imagem/alho.png",70,70,2),
     Obstaculo("imagem/agua.png",70,70,-50),
     Obstaculo("Imagem/cruz.png",60,70, -50)]
     

#Se não colocar em loop a tela do jogo não permanece.
jogo_ligado = True
while jogo_ligado:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jogo_ligado = False
    

    tela.blit (fundo,(0,0))
    tela.blit (morgana.imagem,(morgana.p_x,morgana.p_y))
    

    for ob in o:
        ob.movimento()
        ob.desenho(tela)
        if morgana.masc.overlap(ob.mask,(ob.p_x - morgana.p_x,ob.p_y - morgana.p_y)):
        
            pontuacao = pontuacao + ob.pontuacao
            print(f"Morgana: {pontuacao}")

            ob.p_y = ob.p_yi



    morgana.moviment(pg.K_RIGHT,pg.K_LEFT)
    #Permanencia de atualizações
    pg.display.update()
    r.tick(60)
