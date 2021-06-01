import pygame
import sys
import random

pygame.init()
def fontes(): #PRONTO
    fonteTítulo = pygame.font.SysFont("Jokerman", 42, bold=False, italic=False)
    fonteBotao = pygame.font.SysFont("aclonica", 32)
    fonteContador = pygame.font.SysFont("Microsoft Yi Baiti", 26, bold = True)
    return fonteBotao, fonteTítulo, fonteContador

def def_Tela(): #PRONTO
    tela = pygame.display.set_mode((400,600))
    tela.fill((0,0,0))
    porque_sim = ["NeuroRitmo","Vamos Dançar","Exercitando o Cérebro","Atividade Neural Acontecendo o.O",     \
                   "Fritação Pura","Estou chocado :O","Feito com carinho <3","Just V I B E","Experimento no.3",\
                   "Analisando dados bip--bop//","Crab rave \i=i/","Rave sem neura","Synth a wave",            \
                   "Technomancer x.x","Música><Pensamentos><Se propagando<<>><<>>"]
    a = random.choice(porque_sim)
    pygame.display.set_caption(a)
    return tela

def animacoes_Jogo(): #PRONTO
    # Eletricidade em jogo: 
    estagio1_0 = pygame.image.load("imgs/sprites/estagio1_0.png")
    estagio1_0 = pygame.transform.scale(estagio1_0,[100,600])
    estagio1_1 = pygame.image.load("imgs/sprites/estagio1_1.png")
    estagio1_1 = pygame.transform.scale(estagio1_1,[100,600])
    estagio1_2 = pygame.image.load("imgs/sprites/estagio1_2.png")
    estagio1_2 = pygame.transform.scale(estagio1_2,[100,600])
    estagio2_0 = pygame.image.load("imgs/sprites/estagio2_0.png")
    estagio2_0 = pygame.transform.scale(estagio2_0,[100,600])
    estagio2_1 = pygame.image.load("imgs/sprites/estagio2_1.png")
    estagio2_1 = pygame.transform.scale(estagio2_1,[100,600])
    estagio2_2 = pygame.image.load("imgs/sprites/estagio2_2.png")
    estagio2_2 = pygame.transform.scale(estagio2_2,[100,600])
    estagio3_0 = pygame.image.load("imgs/sprites/estagio3_0.png")
    estagio3_0 = pygame.transform.scale(estagio3_0,[100,600])
    estagio3_1 = pygame.image.load("imgs/sprites/estagio3_1.png")
    estagio3_1 = pygame.transform.scale(estagio3_1,[100,600])
    estagio3_2 = pygame.image.load("imgs/sprites/estagio3_2.png")
    estagio3_2 = pygame.transform.scale(estagio3_2,[100,600])
    AnimaAcerto = pygame.image.load("imgs/sprites/ACERTOraio.png")
    AnimaAcerto = pygame.transform.scale(AnimaAcerto,[100,600])

    eletricidade = [estagio1_0,estagio1_1,estagio1_2,estagio2_0,estagio2_1,estagio2_2,estagio3_0,estagio3_1,estagio3_2]
    return eletricidade, AnimaAcerto
