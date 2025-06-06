import pygame as pg
import random
import time
from personagem import Morgana
from obstaculos import Obstaculo

pg.init() #Configurações iniciais
r = pg.time.Clock()
pontuacao = 0
tela = pg.display.set_mode((1200,800)) #Criando tela
pg.display.set_caption("Lady Morgana") #Nome do jogo

estado = "CAPA"
morgana = Morgana("imagem/morgana__.png",120,208,550,550)
fonte_placar = pg.font.SysFont("Matura MT Script Capitals",25,False,False)

fundo_v = pg.image.load("imagem/vitoria.png")
fundo_v = pg.transform.scale(fundo_v,(1200,820))
fundo_i = pg.image.load("imagem/tutorial.png")
fundo_i = pg.transform.scale(fundo_i,(1200,820))
fundo_c = pg.image.load("imagem/capa.png")
fundo_c = pg.transform.scale(fundo_c,(1200,820))
fundo_d = pg.image.load("imagem/derrota.png")
fundo_d = pg.transform.scale(fundo_d,(1200,820))
fundo = pg.image.load ("imagem/cenario_02.png") #Decidindo o cenário
tela.blit (fundo,(0,0)) #Desenhando o cenário
o = [Obstaculo("imagem/pocao_a.png",70,70,500), #Lista de obstáculos
     Obstaculo("imagem/vinho.png",70,70,2),
     Obstaculo("imagem/morcego.png",80,80,1),
     Obstaculo("imagem/bolsa.png",70,70,6),
     Obstaculo("imagem/sangue.png",70,70,3),
     Obstaculo("imagem/grimorio.png",60,70,2),
     Obstaculo("imagem/pocao_m.png",70,70,-1000),
     Obstaculo("imagem/alho.png",70,70,2),
     Obstaculo("imagem/agua.png",70,70,-50)]
     

#Se não colocar em loop a tela do jogo não permanece.
jogo_ligado = True
while jogo_ligado:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jogo_ligado = False
    
    

    if estado == "CAPA":
        tela.blit(fundo_c,(0,0))
        if evento.type == pg.KEYDOWN:
             if evento.key == pg.K_RETURN:
                  estado = "INSTRUÇÕES"

    elif estado == "INSTRUÇÕES":
        tela.blit(fundo_i,(0,0))
        if evento.type == pg.KEYDOWN:
             if evento.key == pg.K_KP_ENTER:
                  estado = "JOGANDO"

    elif estado == "JOGANDO":
        tela.blit (fundo,(0,0))
        tela.blit (morgana.imagem,(morgana.p_x,morgana.p_y))

        placar_morgana = fonte_placar.render(f"Morgana: {pontuacao}",True, (255,255,255),(0,0,0))
        tela.blit(placar_morgana,(0,0))
        

        for ob in o:
            ob.movimento()
            ob.desenho(tela)
            if morgana.masc.overlap(ob.mask,(ob.p_x - morgana.p_x,ob.p_y - morgana.p_y)):
                pontuacao = pontuacao + ob.pontuacao
                print(f"Morgana: {pontuacao}")
                ob.movimento()
                ob.p_y = ob.p_yi 
                ob.p_x = random.choice(ob.lista_pos)
                if pontuacao <= -3000:
                    estado = "GAME OVER"
            elif pontuacao >= 5000:
                    estado = "VICTORY"

    if estado == "VICTORY":
         tela.blit(fundo_v,(0,0))
    elif estado == "GAME OVER":
         tela.blit(fundo_d,(0,0))
    
        
        


    morgana.moviment(pg.K_RIGHT,pg.K_LEFT)
    #Permanencia de atualizações
    pg.display.update()
    r.tick(60)


#msc de fundo
    #pygame.mixer.music.load("som/musica_fundo.mp3"
    #pygame.mixer.music.set_endevent(pygame.USEREVENT)
    #pygame.mixer.music.play()