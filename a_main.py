import pygame as pg
import random
from personagem import Morgana
from obstaculos import Obstaculo
from caminho_alternativo import caminho_alternativo

pg.init() #Configurações iniciais.
r = pg.time.Clock()
pontuacao = 0
tela = pg.display.set_mode((1200,800)) #Criando tela.

pg.mixer.music.load(caminho_alternativo("som/fundo_som.mp3")) #Aplicando música de fundo.
pg.mixer.music.set_endevent(pg.USEREVENT)
pg.mixer.music.play(loops=-1)

pg.display.set_caption("Lady Morgana") #Nome do jogo.

estado = "CAPA" #Estado em que o jogo se encontra.
morgana = Morgana(caminho_alternativo("imagem/morgana__.png"),120,208,550,550,(caminho_alternativo("som/item_.mp3"))) #Definições do personagem jogável.
fonte_placar = pg.font.SysFont("Castellar",27,False,False)

fundo_v = pg.image.load(caminho_alternativo("imagem/vitoria.png"))
fundo_v = pg.transform.scale(fundo_v,(1200,820))
fundo_i = pg.image.load(caminho_alternativo("imagem/tutorial.png"))
fundo_i = pg.transform.scale(fundo_i,(1200,820))
fundo_c = pg.image.load(caminho_alternativo("imagem/capa_.png"))
fundo_c = pg.transform.scale(fundo_c,(1200,820))
fundo_d = pg.image.load(caminho_alternativo("imagem/derrota.png"))
fundo_d = pg.transform.scale(fundo_d,(1200,820))
fundo = pg.image.load (caminho_alternativo("imagem/cenario_02.png")) #Decidindo o cenário.
tela.blit (fundo,(0,0)) #Desenhando o cenário.
o = [Obstaculo(caminho_alternativo("imagem/pocao_a.png"),70,70,500), #Lista de obstáculos.
     Obstaculo(caminho_alternativo("imagem/vinho.png"),70,70,20),
     Obstaculo(caminho_alternativo("imagem/morcego.png"),80,80,10),
     Obstaculo(caminho_alternativo("imagem/bolsa.png"),70,70,60),
     Obstaculo(caminho_alternativo("imagem/sangue.png"),70,70,10),
     Obstaculo(caminho_alternativo("imagem/grimorio.png"),60,70,20),
     Obstaculo(caminho_alternativo("imagem/pocao_m.png"),70,70,-1000),
     Obstaculo(caminho_alternativo("imagem/alho.png"),70,70,-100),
     Obstaculo(caminho_alternativo("imagem/agua.png"),70,70,-50)]
     

#Se não colocar em loop a tela do jogo não permanece.
jogo_ligado = True
while jogo_ligado:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            jogo_ligado = False
    
    

    if estado == "CAPA": #Estado que mostra a capa, ao selecionar return a tela muda para o tutorial.
        tela.blit(fundo_c,(0,0))
        if evento.type == pg.KEYDOWN:
             if evento.key == pg.K_RETURN:
                  estado = "INSTRUÇÕES"

    elif estado == "INSTRUÇÕES":  #Estado que mostra o tutorial, ao selecionar enter a tela muda para o jogo.
        tela.blit(fundo_i,(0,0))
        if evento.type == pg.KEYDOWN:
             if evento.key == pg.K_KP_ENTER:
                  estado = "JOGANDO"

    elif estado == "JOGANDO": #Estado em que o jogo ocorre.
        tela.blit (fundo,(0,0))
        tela.blit (morgana.imagem,(morgana.p_x,morgana.p_y))

        placar_morgana = fonte_placar.render(f"Morgana: {pontuacao}",True, (255,255,255))
        tela.blit(placar_morgana,(0,5))
        

        for ob in o:
            ob.movimento()
            ob.desenho(tela)
            if morgana.masc.overlap(ob.mask,(ob.p_x - morgana.p_x,ob.p_y - morgana.p_y)):
                pontuacao = pontuacao + ob.pontuacao
                print(f"Morgana: {pontuacao}")
                morgana.som.play()
                ob.movimento()
                ob.p_y = ob.p_yi 
                ob.p_x = random.choice(ob.lista_pos)
                if pontuacao <= -3000:
                    pg.mixer.music.stop()
                    estado = "GAME OVER"
                    pg.mixer.music.load(caminho_alternativo("som/grito_.mp3")) #Trocando música de fundo.
                    pg.mixer.music.set_endevent(pg.USEREVENT)
                    pg.mixer.music.play()
            elif pontuacao >= 5000:
                    pg.mixer.music.stop()
                    estado = "VICTORY"
                    pg.mixer.music.load(caminho_alternativo("som/risada_.mp3")) #Trocando música de fundo.
                    pg.mixer.music.set_endevent(pg.USEREVENT)
                    pg.mixer.music.play()
        


    if estado == "VICTORY":
         tela.blit(fundo_v,(0,0))
        
    elif estado == "GAME OVER":
         tela.blit(fundo_d,(0,0))
         

    
        
        


    morgana.moviment(pg.K_RIGHT,pg.K_LEFT)
    #Permanencia de atualizações
    pg.display.update()
    r.tick(60)