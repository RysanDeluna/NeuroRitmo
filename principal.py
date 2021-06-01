import pygame
import sys
from jogo import __jogo, feedback
from menu import menu_Principal, __créditos, __instruções
pygame.init()
sair = False
seleção = "menu"
while not sair: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        # redireciona para as telas do jogo
        elif seleção == "menu":
            seleção = menu_Principal()
        elif seleção == "joguinho":
            pontos = __jogo() 
            seleção = feedback(pontos)
        elif seleção == "créditos":
            seleção = __créditos()
        elif seleção == "instruções":
            seleção = __instruções()
pygame.quit()
# // Feito por Ryan Marco Andrade dos Santos, TIA: 42080223
