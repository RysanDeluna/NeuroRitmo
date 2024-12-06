import pygame, sys
from funcoes import def_Tela, fontes
pygame.init()

def main_menu(): #PRONTO
    # definições da window
    window = def_Tela()

    # carregando as imagens da window inicial
    bg = pygame.image.load("imgs/planoDeFundo/bg200.png")
    bg = pygame.transform.scale(bg,[400,600])
    button1 = pygame.image.load("imgs/botoes/Botao1x.png")
    button1 = pygame.transform.scale(button1,[135,50])
    button2 = pygame.image.load("imgs/botoes/Botao2x.png")
    button2 = pygame.transform.scale(button2, [45,45])

    # Definindo a Fonte e Renderizando
    button_font, title_font, counter_font = fontes()
    game_title = title_font.render("NeuroRitmo", True, (255,215,0))
    play_b = button_font.render("JOGAR", True, (255,99,71))
    quit_b = button_font.render("X", True, (255,99,71))
    instructions_b = button_font.render("?", True, (255,99,71))
    credits_b = button_font.render("CRÉDITOS", True, (255,99,71))

    # definição dos elementos da window
    window.blit(bg,(0,0))
    window.blit(button1,(92,257))
    window.blit(button1,(92,320))
    window.blit(button2,(339,485))
    window.blit(button2,(339,543))
    window.blit(game_title,[118,100])
    window.blit(play_b,[120,274])
    window.blit(quit_b,[354,556])
    window.blit(instructions_b,[354,499])
    window.blit(credits_b, [102,333])
    pygame.display.update()

    # Carregando sons
    press_button = pygame.mixer.Sound("audios/selecao.wav")
    pygame.mixer.music.load("audios/temaPrin.mp3")

    quit_flag = False
    while not quit_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # vai para as próximas telas
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x>=92 and x<=227 and y>=257 and y<=307:
                    press_button.play()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    return "joguinho"
                if x>=92 and x<=227 and y>=321 and y<=367:
                    press_button.play()
                    pygame.mixer.music.stop()   
                    pygame.mixer.music.unload()
                    return "créditos"
                if x>=346 and x<=377 and y>=491 and y<=524:
                    press_button.play()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    return "instruções"
                if x>=346 and x<=377 and y>=550 and y<=580:
                    pygame.quit()
                    sys.exit()
        # Mantém a música em loop
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()

def __credits(): #PRONTO
    window = def_Tela()
    selection = pygame.mixer.Sound("audios/selecao.wav")
    pygame.mixer.music.load("audios/temaPrin.mp3")

    bg = pygame.image.load("imgs/planoDeFundo/bgCRED.png")
    bg = pygame.transform.scale(bg,[400,600])
    smiley = pygame.image.load("imgs/objetos/smileyy.png")
    smiley = pygame.transform.scale(smiley,[36,54])

    fonte = pygame.font.SysFont("Californian FB",15)
    fonteN = pygame.font.SysFont("Californian FB", 16, bold=True)
    fonteT = pygame.font.SysFont("Jokerman", 24)
    fonteBotao = pygame.font.SysFont("OCR A Extended", 30, bold=True)
    creditos1 = fonte.render("Projeto - Algoritmos e Programação 2", True, (255,215,0))
    creditos2 = fonte.render("Univerdade Presbiteriana Mackenzie",True, (255,215,0))
    creditos3 = fonteT.render("NEURORITMO", True, (255,215,0))
    creditos4 = fonteN.render("Desenvolvido e idealizado por:", True, (255,215,0))
    creditos5 = fonte.render("Ryan Marco Andrade dos Santos", True, (255,215,0))
    creditos6 = fonteN.render("Músicas e efeitos utilizados:", True, (255,215,0))
    creditos7 = fonte.render("-Música de Fundo: Disco Descent(1-1) ", True, (255,215,0))
    creditos8 = fonte.render("-Efeitos sonoros por: LittleBotSoundFactory ", True, (255,215,0))
    creditos9 = fonte.render("-Resultado da partida: Honeybone82", True, (255,215,0))
    quit_b = fonteBotao.render("X", True, (249,120,90))

    m_button = pygame.image.load("imgs/botoes/Botao2x.png")
    m_button = pygame.transform.scale(m_button,[45,45])

    window.blit(bg,(0,0))
    window.blit(creditos1,(101,112))
    window.blit(creditos2,(101,139))
    window.blit(creditos3,(130,197))
    window.blit(creditos4,(101,272))
    window.blit(creditos5,(116,312))
    window.blit(creditos6,(110,352))
    window.blit(creditos7,(94,392))
    window.blit(creditos8,(79,419))
    window.blit(creditos9,(94,446))
    window.blit(m_button,(300,545))
    window.blit(quit_b, (312,550))
    window.blit(smiley,(133,470))
    pygame.display.update()


    quit_flag = False
    while not quit_flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_flag = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x>=300 and x<=345 and y>=545 and y<=590:
                    selection.play()
                    quit_flag = True

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
    return "menu"

def __instructions(): #PRONTO
    window = def_Tela()
    selection = pygame.mixer.Sound("audios/selecao.wav")
    pygame.mixer.music.load("audios/temaPrin.mp3")

    fonte = pygame.font.SysFont("Californian FB",17)
    fonteN = pygame.font.SysFont("Californian FB", 17, bold=True)
    fonteT = pygame.font.SysFont("Jokerman", 24)
    fonteE = pygame.font.SysFont("Viner Hand ITC",26, bold=False)
    fonteBotao = pygame.font.SysFont("OCR A Extended", 30, bold=True)
    quit_b = fonteBotao.render("X", True, (249,120,90))

    titulo = fonteT.render("COMO JOGAR", True, (255,215,0))
    inst1 = fonte.render("Iremos pensar ao ritmo da música :)", True, (255,215,0))
    inst2 = fonte.render("Haverão 4 neurônios presentes na window;", True, (255,215,0))
    inst3 = fonte.render("cada célula tem uma tecla respectiva", True, (255,215,0))
    inst4 = fonte.render("as quais são:", True, (255,215,0))
    inst5 = fonteN.render("D    F    J    K", True, (255,215,0))
    inst6 = fonte.render("Aperte a tecla onde há estímulos...", True, (255,215,0))
    inst7 = fonteE.render("Elétricos!", True, (255,215,0))

    bg = pygame.image.load("imgs/planoDeFundo/bgCRED.png")
    bg = pygame.transform.scale(bg,[400,600])
    m_button = pygame.image.load("imgs/botoes/Botao2x.png")
    m_button = pygame.transform.scale(m_button,[45,45])

    window.blit(bg,(0,0))
    window.blit(titulo,(130,170))
    window.blit(inst1,(85,235))
    window.blit(inst2,(75,260))
    window.blit(inst3,(75,285))
    window.blit(inst4,(75,310))
    window.blit(inst5,(176,311))
    window.blit(inst6,(75,335))
    window.blit(inst7,(162,385))
    window.blit(m_button,(300,545))
    window.blit(quit_b, (312,550))

    pygame.display.update()

    quit_flag = False
    while not quit_flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    quit_flag = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x>=300 and x<=345 and y>=545 and y<=590:
                    selection.play()
                    quit_flag = True

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
    return "menu"
