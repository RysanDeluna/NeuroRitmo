import asyncio
import pygame
from jogo import __jogo, feedback
from menu import main_menu, __credits, __instructions

pygame.init()
quitting = False
selection = "menu"


async def main():
    global quitting, selection
    while not quitting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitting = True
            # redireciona para as telas do jogo
            elif selection == "menu":
                selection = main_menu()
            elif selection == "joguinho":
                pontos = __jogo()
                selection = feedback(pontos)
            elif selection == "créditos":
                selection = __credits()
            elif selection == "instruções":
                selection = __instructions()
        await asyncio.sleep(0)
    return True

asyncio.run(main())
# // Made by Ryan Marco Andrade dos Santos, TIA: 42080223
