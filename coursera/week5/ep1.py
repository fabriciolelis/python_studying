def computador_escolhe_jogada(n, m):
    resto = n % (m + 1)
    if 0 < resto <= m:
        quant_ret = resto
    else:
        quant_ret = m
    print("O computador tirou um peça" if quant_ret == 1 else "O computador tirou", quant_ret, "peças")
    return quant_ret


def usuario_escolhe_jogada(n, m):
    quant_ret = int(input("Quantas peças você vai tirar? "))
    print()
    nao_eh_valida = True
    while nao_eh_valida:
        if quant_ret > m or quant_ret <= 0 or quant_ret > n:
            print("Opps! Jogada inválida! tente de novo.")
            quant_ret = int(input("Quantas peças você vai tirar? "))
        else:
            nao_eh_valida = False
    print("Você tirou um peça" if quant_ret == 1 else "Você tirou", quant_ret, "peças")
    return quant_ret


def partida():
    print("Você escolheu partida isolada!")
    quant_pecas = int(input("Quantas Peças? "))
    limite_pecas = int(input("Limite de peças por jogada? "))
    bad_value = True
    if (limite_pecas > 0):
        bad_value = False
    while bad_value:
        limite_pecas = int(input("Limite de peças por jogada? "))
        if limite_pecas > 0:
            bad_value = False
    if quant_pecas % (limite_pecas + 1) == 0:
        print("Você começa")
        print()
        quant_pecas = quant_pecas - usuario_escolhe_jogada(quant_pecas, limite_pecas)
        euJoguei = True
    else:
        print("Computador começa")
        print()
        quant_pecas = quant_pecas - computador_escolhe_jogada(quant_pecas, limite_pecas)
        euJoguei = False
    while quant_pecas > 0:
        if (quant_pecas == 1):
            print("Agora resta apenas uma peça no tabuleiro")
        else:
            print("Agora restam", quant_pecas, "peças no tabuleiro")
        if (euJoguei):
            quant_pecas = quant_pecas - computador_escolhe_jogada(quant_pecas, limite_pecas)
            euJoguei = False
        else:
            quant_pecas = quant_pecas - usuario_escolhe_jogada(quant_pecas, limite_pecas)
            euJoguei = True
    if (euJoguei):
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
        if (limitePecas > 0):
            badValue = False
        while badValue:
            limitePecas = int(input("Limite de peças por jogada? "))
            if (limitePecas > 0):
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
            if (quantPecas == 1):
                print("Agora resta apenas uma peça no tabuleiro")
            else:
                print("Agora restam", quantPecas, "peças no tabuleiro")
            if (euJoguei):
                quantPecas = quantPecas - computador_escolhe_jogada(quantPecas, limitePecas)
                euJoguei = False
            else:
                quantPecas = quantPecas - usuario_escolhe_jogada(quantPecas, limitePecas)
                euJoguei = True
        if (euJoguei):
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
