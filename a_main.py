import pygame as pg
pg.init() #Configurações iniciais
r = pg.time.Clock()

tela = pg.display.set_mode((1200,800)) #Criando tela
pg.display.set_caption("Lady Morgana") #Nome do jogo

#Se não colocar em loop a tela do jogo não permanece.
jogo_ligado = True
while jogo_ligado:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jogo_ligado = False


    #Permanencia de atualizações
    pg.display.update()
    r.tick(60)