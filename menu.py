import pygame, sys
from funcoes import def_Tela, fontes
pygame.init()

def menu_Principal(): #PRONTO
    # definições da tela
    tela = def_Tela()

    # carregando as imagens da tela inicial
    bg = pygame.image.load("imgs/planoDeFundo/bg200.png")
    bg = pygame.transform.scale(bg,[400,600])
    botao1 = pygame.image.load("imgs/botoes/Botao1x.png")
    botao1 = pygame.transform.scale(botao1,[135,50])
    botao2 = pygame.image.load("imgs/botoes/Botao2x.png")
    botao2 = pygame.transform.scale(botao2, [45,45])

    # Definindo a Fonte e Renderizando
    fonteBotao, fonteTitulo, fonteContador = fontes()
    tituloJogo = fonteTitulo.render("NeuroRitmo", True, (255,215,0))
    Bjogar = fonteBotao.render("JOGAR", True, (255,99,71))
    Bsair = fonteBotao.render("X", True, (255,99,71))
    Binstru = fonteBotao.render("?", True, (255,99,71))
    Bcred = fonteBotao.render("CRÉDITOS", True, (255,99,71))

    # definição dos elementos da tela 
    tela.blit(bg,(0,0))
    tela.blit(botao1,(92,257))
    tela.blit(botao1,(92,320))
    tela.blit(botao2,(339,485))
    tela.blit(botao2,(339,543))
    tela.blit(tituloJogo,[118,100])
    tela.blit(Bjogar,[120,274])
    tela.blit(Bsair,[354,556])
    tela.blit(Binstru,[354,499])
    tela.blit(Bcred, [102,333])
    pygame.display.update()

    # Carregando sons
    aperta_botao = pygame.mixer.Sound("audios/selecao.wav")
    pygame.mixer.music.load("audios/temaPrin.mp3")

    sair = False
    while not sair: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # vai para as próximas telas
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x>=92 and x<=227 and y>=257 and y<=307:
                    aperta_botao.play()   
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    return "joguinho"
                if x>=92 and x<=227 and y>=321 and y<=367:
                    aperta_botao.play()
                    pygame.mixer.music.stop()   
                    pygame.mixer.music.unload()
                    return "créditos"
                if x>=346 and x<=377 and y>=491 and y<=524:
                    aperta_botao.play()   
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    return "instruções"
                if x>=346 and x<=377 and y>=550 and y<=580:
                    pygame.quit()
                    sys.exit()
        # Mantém a música em loop
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()

def __créditos(): #PRONTO 
    tela = def_Tela()
    selecao = pygame.mixer.Sound("audios/selecao.wav")
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
    Bsair = fonteBotao.render("X", True, (249,120,90))

    botaoM = pygame.image.load("imgs/botoes/Botao2x.png")
    botaoM = pygame.transform.scale(botaoM,[45,45])

    tela.blit(bg,(0,0))
    tela.blit(creditos1,(101,112))
    tela.blit(creditos2,(101,139))
    tela.blit(creditos3,(130,197))
    tela.blit(creditos4,(101,272))
    tela.blit(creditos5,(116,312))
    tela.blit(creditos6,(110,352))
    tela.blit(creditos7,(94,392))
    tela.blit(creditos8,(79,419))
    tela.blit(creditos9,(94,446))
    tela.blit(botaoM,(300,545))
    tela.blit(Bsair, (312,550))
    tela.blit(smiley,(133,470))
    pygame.display.update()


    sair = False
    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x>=300 and x<=345 and y>=545 and y<=590:
                    selecao.play()
                    sair = True

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
    return "menu"

def __instruções(): #PRONTO
    tela = def_Tela()
    selecao = pygame.mixer.Sound("audios/selecao.wav")
    pygame.mixer.music.load("audios/temaPrin.mp3")

    fonte = pygame.font.SysFont("Californian FB",17)
    fonteN = pygame.font.SysFont("Californian FB", 17, bold=True)
    fonteT = pygame.font.SysFont("Jokerman", 24)
    fonteE = pygame.font.SysFont("Viner Hand ITC",26, bold=False)
    fonteBotao = pygame.font.SysFont("OCR A Extended", 30, bold=True)
    Bsair = fonteBotao.render("X", True, (249,120,90))

    titulo = fonteT.render("COMO JOGAR", True, (255,215,0))
    inst1 = fonte.render("Iremos pensar ao ritmo da música :)", True, (255,215,0))
    inst2 = fonte.render("Haverão 4 neurônios presentes na tela;", True, (255,215,0))
    inst3 = fonte.render("cada célula tem uma tecla respectiva", True, (255,215,0))
    inst4 = fonte.render("as quais são:", True, (255,215,0))
    inst5 = fonteN.render("D    F    J    K", True, (255,215,0))
    inst6 = fonte.render("Aperte a tecla onde há estímulos...", True, (255,215,0))
    inst7 = fonteE.render("Elétricos!", True, (255,215,0))

    bg = pygame.image.load("imgs/planoDeFundo/bgCRED.png")
    bg = pygame.transform.scale(bg,[400,600])
    botaoM = pygame.image.load("imgs/botoes/Botao2x.png")
    botaoM = pygame.transform.scale(botaoM,[45,45])

    tela.blit(bg,(0,0))
    tela.blit(titulo,(130,170))
    tela.blit(inst1,(85,235))
    tela.blit(inst2,(75,260))
    tela.blit(inst3,(75,285))
    tela.blit(inst4,(75,310))
    tela.blit(inst5,(176,311))
    tela.blit(inst6,(75,335))
    tela.blit(inst7,(162,385))
    tela.blit(botaoM,(300,545))
    tela.blit(Bsair, (312,550))

    pygame.display.update()

    sair = False
    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x>=300 and x<=345 and y>=545 and y<=590:
                    selecao.play()
                    sair = True

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
    return "menu"
