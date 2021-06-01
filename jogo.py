import pygame, random, sys, time
from funcoes import fontes, def_Tela, animacoes_Jogo

def telaJogo(): #PRONTO
    tela = def_Tela()
    # Carregando imagens de jogo
    bgJOOJ = pygame.image.load("imgs/planoDeFundo/bgJOOJ.png")
    bgJOOJ = pygame.transform.scale(bgJOOJ,[400,600])
    celulasAlvo = pygame.image.load("imgs/objetos/celulasJogo.png")
    celulasAlvo = pygame.transform.scale(celulasAlvo,[400,600])
    botao = pygame.image.load("imgs/sprites/bJogo1.png")
    botao = pygame.transform.scale(botao,[102,60])
    botaoPressionado = pygame.image.load("imgs/sprites/bJogo2.png")
    botaoPressionado = pygame.transform.scale(botaoPressionado,[102,60])
    return tela, bgJOOJ, celulasAlvo, botao, botaoPressionado

def randomizator(contadorAlvo, pistas): #PRONTO
    # Determina a cada quantos clocks, nesta instância, será requisitada uma nova nota
    aleatorizador = random.randint(3,12)  # Quanto menor estes valores, mais difícil fica
    alvo = None
    auxiliaNator = None # Impede que a mesma nota se repita naquela instância
    # Aleatoriza uma nova nota a cada "x" clocks
    if contadorAlvo/aleatorizador == contadorAlvo//aleatorizador:
        alvo = random.choice(pistas)
        while alvo == auxiliaNator:
            alvo = random.choice(pistas)
    return alvo

def contadorPontos(pontos, fonteCont, qntAcertos, qntErros): #PRONTO
    # Renderiza os textos para os placares de acordo com a quantidade de pontos, erros e acertos e retorna esses textos
    pontuacao = fonteCont.render("QI:"+str(pontos), True,(75,0,130))
    acertos = fonteCont.render("Acertos:"+str(qntAcertos), True, (75,0,130))
    erros = fonteCont.render("Erros:"+str(qntErros), True, (75,0,130))
    return pontuacao, acertos, erros

def contagemINIcio(tela, bgJOOJ, som): #PRONTO
    # Define a lista de elementos para contagem
    contagem = ["  3","  2","  1","Vai!"]
    # Define a fonte
    font_contagem_para_inicio = pygame.font.SysFont("Tempus Sans ITC", 60)
    # Carrega e dimensiona o botão de fundo
    quadro = pygame.image.load("imgs/botoes/Botao2x.png")
    quadro = pygame.transform.scale(quadro,[200,200])
    # Laço para a impressão dos números
    for i in contagem:
        # Permite que o jogo seja fechado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Renderiza o texto de acordo com a lista criada anteriormente
        contagem_para_inicio = font_contagem_para_inicio.render(i, True, (220,20,60))
        # Atualização da tela
        tela.blit(bgJOOJ,(0,0))
        tela.blit(quadro,(100,175))
        tela.blit(contagem_para_inicio,(151,240))
        pygame.display.update()
        # Sonzinho legal :D
        som.play()
        # Aguarda 1 segundo
        pygame.time.delay(1000)

def sonsJogo(): #PRONTO
    som_erro = pygame.mixer.Sound("audios/erro.mp3")
    som_acerto = pygame.mixer.Sound("audios/acerto.wav")
    som_contagem = pygame.mixer.Sound("audios/contagem.wav")
    pygame.mixer.music.load("audios/cryptOfTheNeuroDancer.mp3")
    return som_acerto, som_erro, som_contagem

def feedback(pontos): #PRONTO
    tela = def_Tela()
    # Fontes e sentenças a serem utilizadas
    fonte = pygame.font.SysFont("OCR A Extended", 40)
    fonteBotao = pygame.font.SysFont("OCR A Extended", 30, bold=True)
    qi = fonte.render(str(pontos), True, (173,216,230))
    Bsair = fonteBotao.render("X", True, (249,120,90))
    # Carregamento e dimensionamento de imagens
    botaoM = pygame.image.load("imgs/botoes/Botao2x.png")
    botaoM = pygame.transform.scale(botaoM,[45,45])
    bg = pygame.image.load("imgs/planoDeFundo/feedback.png")
    bg = pygame.transform.scale(bg,[400,600])
    botaoJogarNovamente = pygame.image.load("imgs/botoes/BotaoRetorno.png")
    botaoJogarNovamente = pygame.transform.scale(botaoJogarNovamente,[45,45])
    # Carregamento de sons
    selecao = pygame.mixer.Sound("audios/selecao.wav")
    pygame.mixer.music.load("audios/victoryyy.wav")
    # Atualização da tela
    tela.blit(bg,(0,0))
    tela.blit(botaoM,(300,545))
    tela.blit(qi, (198,138))
    tela.blit(Bsair, (312,550))
    tela.blit(botaoJogarNovamente,(252,545))
    pygame.display.update()
    # Interações
    sair = False
    while not sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x>=300 and x<=345 and y>=545 and y<=590:
                    selecao.play()
                    sair = True
                if x>=252 and x<=297 and y>=545 and y<=590:
                    selecao.play()
                    return "joguinho"
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.7)
    return "menu"

def __jogo(): #PRONTO
    #definições de variáveis que serão utilizadas
    alvo = None
    contadorAlvo = 0
    pontos = 0
    pistas = [0,1,2,3,None,None]
    i = 0
    erros = 0
    acertos = 0
    
    #Funções chamadas
    tela, bgJOOJ, celulasAlvo, botao, botaoPessionado = telaJogo()
    som_acerto, som_erro, som_contagem = sonsJogo()
    sprite, animacao_acerto = animacoes_Jogo()
    fonteBotao, fonteTitulo, fonteContador = fontes()
    contagemINIcio(tela, bgJOOJ, som_contagem)
    
    #Ajeitando Sons
    pygame.mixer.Sound.set_volume(som_acerto, 0.4)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1.0)
    
    #Indicação das teclas
    D1 = fonteBotao.render("D", True, (223,113,38))
    D2 = fonteBotao.render("D", True, (31,99,113))
    F1 = fonteBotao.render("F", True, (223,113,38))
    F2 = fonteBotao.render("F", True, (31,99,113))
    J1 = fonteBotao.render("J", True, (223,113,38))
    J2 = fonteBotao.render("J", True, (31,99,113))
    K1 = fonteBotao.render("K", True, (223,113,38))
    K2 = fonteBotao.render("K", True, (31,99,113))

    while pygame.mixer.music.get_busy():        
        # Clock
        clock = pygame.time.Clock()
        clock.tick(30)
        # Aleatoriza qual dos botões do jogador deverá apertar
        contadorAlvo += 1    
        alvo = randomizator(contadorAlvo, pistas) 
        verificador = False
        # MECÂNICA E ANIMAÇÕES
        if alvo != None:
            # Mantém o jogo junto às animações para que os comandos possam ser feitos simultaneamente
            # ao carregamento dos sprites
            for i in sprite:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    # VERIFICAÇÃO DE ACERTO
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            # efeito visual para indicar que o botão foi pressionado
                            tela.blit(botaoPessionado,(0,525))
                            tela.blit(D2,(45,545))
                            if alvo == 0:  #ACERTO
                                tela.blit(animacao_acerto,(0,80))
                                pontos += 1
                                acertos += 1
                                som_acerto.play()
                                verificador = True
                            else:          #ERRO
                                pontos -= 1
                                erros +=1
                                som_erro.play()
                        elif event.key == pygame.K_f:
                            tela.blit(F2,(145,545))
                            tela.blit(botaoPessionado,(100,525))
                            if alvo == 1: #ACERTO
                                tela.blit(animacao_acerto,(98,80))                            
                                pontos += 1
                                acertos += 1
                                som_acerto.play()
                                verificador = True
                            else:        #ERRO
                                pontos -= 1
                                erros +=1
                                som_erro.play()
                        elif event.key == pygame.K_j:
                            tela.blit(botaoPessionado,(200,525))
                            tela.blit(J2,(245,545))
                            if alvo == 2:  #ACERTO
                                tela.blit(animacao_acerto,(200,80))                            
                                pontos += 1
                                acertos += 1
                                som_acerto.play()
                                verificador = True
                            else:          #ERRO
                                pontos -= 1
                                erros +=1
                                som_erro.play()
                        elif event.key == pygame.K_k:
                            tela.blit(botaoPessionado,(300,525))
                            tela.blit(K2,(345,545))
                            if alvo == 3:  #ACERTO
                                tela.blit(animacao_acerto,(294,80))                           
                                pontos += 1    
                                acertos += 1
                                som_acerto.play()
                                verificador = True
                            else:         #ERRO
                                pontos -= 1
                                erros +=1
                                som_erro.play()
                        # CÓDIGO SECRETO :o
                        elif event.key == (pygame.K_v and pygame.K_i and pygame.K_b and pygame.K_e):
                            pygame.mixer.music.stop()
                # Atualizações da tela
                pontuacao, contAcertos, contErros = contadorPontos(pontos, fonteContador, acertos, erros)
                tela.blit(i, (alvo*97,80))        
                pygame.display.update()
                tela.blit(bgJOOJ,(0,0))
                tela.blit(celulasAlvo,(0,80))
                for i in range(0,400,100):
                    tela.blit(botao,(i,525))
                tela.blit(D1, (45,545))
                tela.blit(F1, (145,545))
                tela.blit(J1, (245,545))
                tela.blit(K1, (345,545))
                pygame.draw.rect(tela, (165,42,42), ([0,0],[400,80]))
                pygame.draw.rect(tela, (218,165,32), ([10,10],[380,60]))
                tela.blit(pontuacao,(20,20))
                tela.blit(contAcertos, (120,20))
                tela.blit(contErros, (270,20))
                pygame.time.delay(45)
                pygame.display.update()
            # Verifica se a pessoa apertou algum botão, caso contrário, disconta pontos
            if not verificador:
                pontos -= 1
                erros += 1 
                som_erro.play()
    pygame.time.delay(500)
    return pontos
