import pygame as pg
from personagem import Morgana
from obstaculos import Obstaculo
pg.init() #Configurações iniciais
r = pg.time.Clock()

tela = pg.display.set_mode((1200,800)) #Criando tela
pg.display.set_caption("Lady Morgana") #Nome do jogo


morgana = Morgana("imagem/morgana_.png",140,235,550,550)

fundo = pg.image.load ("imagem/cenario_02.png") #Decidindo o cenário
tela.blit (fundo,(0,0)) #Desenhando o cenário
o = [Obstaculo("imagem/pocao_a.png",70,70),
     Obstaculo("imagem/pocao_m.png",70,70),
     Obstaculo("imagem/vinho.png",70,70),
     Obstaculo("imagem/agua.png",70,70),
     Obstaculo("imagem/morcego.png",80,80)]
     

#Se não colocar em loop a tela do jogo não permanece.
jogo_ligado = True
while jogo_ligado:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jogo_ligado = False
    

    tela.blit (fundo,(0,0))
    tela.blit (morgana.imagem,(morgana.p_x,morgana.p_y))
    for ob in o:
        tela.blit (ob.imagem,(ob.p_x,ob.p_y))

    morgana.moviment(pg.K_RIGHT,pg.K_LEFT)
    #Permanencia de atualizações
    pg.display.update()
    r.tick(60)