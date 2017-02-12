def computador_escolhe_jogada(n, m):
    resto = n % (m + 1)
    if(resto > 0 and resto <= m):
        quantRet = resto
    else:
        quantRet = m
    if(quantRet == 1):
        print("O computador tirou um peça")
    else:
        print("O computador tirou", quantRet, "peças")
    return quantRet

def usuario_escolhe_jogada(n, m):
    quantRet = int(input("Quantas peças você vai tirar? "))
    print()
    naoEhValida = True
    while(naoEhValida):
        if(quantRet > m or quantRet <= 0):
            print("Opps! Jogada inválida! tente de novo.")
            quantRet = int(input("Quantas peças você vai tirar? "))
        else:
            naoEhValida = False
    if(quantRet == 1):
        print("Você tirou um peça")
    else:
        print("Você tirou", quantRet, "peças")
    return quantRet

def partida():
    print("Você escolheu partida isolada!")
    quantPecas = int(input("Quantas Peças? "))
    limitePecas = int(input("Limite de peças por jogada? "))
    badValue = True
    if(limitePecas > 0 and limitePecas < quantPecas):
        badValue = False
    while badValue:
        limitePecas = int(input("Limite de peças por jogada? "))
        if(limitePecas > 0 or limitePecas < quantPecas):
            badValue = False
    if(quantPecas % (limitePecas + 1) == 0):
        print("Você começa")
        print()
        quantPecas = quantPecas - usuario_escolhe_jogada(quantPecas, limitePecas)
        euJoguei = True
    else:
        print("Computador começa")
        print()
        quantPecas = quantPecas - computador_escolhe_jogada(quantPecas, limitePecas)
        euJoguei = False
    while quantPecas > 0:
        if(quantPecas == 1):
            print("Agora resta apenas uma peça no tabuleiro")
        else:
            print("Agora restam", quantPecas, "peças no tabuleiro")
        if(euJoguei):
            quantPecas = quantPecas - computador_escolhe_jogada(quantPecas, limitePecas)
            euJoguei = False
        else:
            quantPecas = quantPecas - usuario_escolhe_jogada(quantPecas, limitePecas)
            euJoguei = True
    if(euJoguei):
        print("Fim de jogo!! Você ganhou")
    else:
        print("Fim de jogo!! O computador ganhou!")

def campeonato():
    rodada = 1
    minhasVitorias = 0
    vitoriasPC = 0
    print("Você escolheu um campeonato!")
    print()
    while rodada <= 3:
        print("**** Rodada ", rodada, " ****")
        print()
        quantPecas = int(input("Quantas peças? "))
        limitePecas = int(input("Limite de peças por jogada? "))
        badValue = True
        if(limitePecas > 0 and limitePecas < quantPecas):
            badValue = False
        while badValue:
            limitePecas = int(input("Limite de peças por jogada? "))
            if(limitePecas > 0 and limitePecas < quantPecas):
                badValue = False
        if (quantPecas % (limitePecas + 1) == 0):
            print("Você começa")
            print()
            quantPecas = quantPecas - usuario_escolhe_jogada(quantPecas, limitePecas)
            euJoguei = True
        else:
            print("Computador começa")
            print()
            quantPecas = quantPecas - computador_escolhe_jogada(quantPecas, limitePecas)
            euJoguei = False
        while quantPecas > 0:
            if(quantPecas == 1):
                print("Agora resta apenas uma peça no tabuleiro")
            else:
                print("Agora restam", quantPecas, "peças no tabuleiro")
            if(euJoguei):
                quantPecas = quantPecas - computador_escolhe_jogada(quantPecas, limitePecas)
                euJoguei = False
            else:
                quantPecas = quantPecas - usuario_escolhe_jogada(quantPecas, limitePecas)
                euJoguei = True
        if(euJoguei):
            print("Fim de Jogo!! Você ganhou!")
            minhasVitorias += 1
        else:
            print("Fim de Jogo!! O computador ganhou")
            vitoriasPC += 1
        rodada += 1
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você ", minhasVitorias, " X ", vitoriasPC, " Computador")


def main():
    opção = int(input("""Bem-vindo ao jogo do NIM! Escolha:
1 - para jogar uma partida isolada
2 - para jogar campeonato """))
    if opção == 1:
        partida()
    else:
        campeonato()

main()
