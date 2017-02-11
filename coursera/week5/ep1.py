def computador_escolhe_jogada(n, m):
    return n - m

def usuario_escolhe_jogada(n, m):
    quantRet = int(input("Quantas peças você vai tirar? "))
    print()
    naoEhValida = True
    while(naoEhValida):
        if(quantRet > m or quantRet > n):
            print("Opps! Jogada inválida! tente de novo.")
            quantRet = int(input("Quantas peças você vai tirar?"))
        else:
            naoEhValida = False
            if(quantRet == 1):
                print("Você tirou um peça")
            else:
                print("Você tirou ", quantRet, " peças")
    return quantRet

def partida():
    rodada = 1;
    opção = int(input("""Bem-vindo ao jogo do NIM! Escolha:
1 - para jogar uma partida isolada
2 - para jogar campeonato """))
    if opção == 1:
        print("Você escolheu partida isolada!")
        quantPecas = int(input("Quantas Pecas? "))
        limitePecas = int(input("Limite de peças por jogada? "))
        if(quantPecas % (limitePecas + 1) == 0):
            print("Você começa")
            print()
            quantPecas = usuario_escolhe_jogada(quantPecas, limitePecas)
            euJoguei = True
        else:
            print("Computador começa")
            print()
            quantPecas = computador_escolhe_jogada(quantPecas,  limitePecas)
            euJoguei = False
        while quantPecas > 0:
            if(quantPecas == 1):
                print("Agora resta apenas uma peça no tabuleiro")
            if(euJoguei):
                quantPecas = computador_escolhe_jogada(quantPecas, limitePecas)
                euJoguei = False
            else:
                quantPecas = usuario_escolhe_jogada(quantPecas,  limitePecas)
                euJoguei = True
        if(euJoguei):
            print("Fim do Jogo!! Eu ganhei")
        else:
            print("Fim do Jogo!! O computador ganhou!")
    else:
        print("Você escolheu um campeonato!")
        print()
        print("**** Rodada ", rodada, " ****")
        print()
        quantPecas = int(input("Quantas peças? "))
        limitePecas = int(input("Limite de peças por jogada? "))
        if quantPecas % (limitePecas + 1) == 0:
            print("Você começa")
            print()
            quantPecas = usuario_escolhe_jogada(quantPecas, limitePecas)
        else:
            print("Computador começa")
            print()
            #computador_escolhe_jogada(quantPecas, limitePecas)
        rodada =+ 1
        while quantPecas < 0:
            if(quantPecas == 1):
                print("Agora resta apenas uma peça no tabuleiro")

partida()
