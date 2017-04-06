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
        eu_joguei = True
    else:
        print("Computador começa")
        print()
        quant_pecas = quant_pecas - computador_escolhe_jogada(quant_pecas, limite_pecas)
        eu_joguei = False
    while quant_pecas > 0:
        if (quant_pecas == 1):
            print("Agora resta apenas uma peça no tabuleiro")
        else:
            print("Agora restam", quant_pecas, "peças no tabuleiro")
        if (eu_joguei):
            quant_pecas = quant_pecas - computador_escolhe_jogada(quant_pecas, limite_pecas)
            eu_joguei = False
        else:
            quant_pecas = quant_pecas - usuario_escolhe_jogada(quant_pecas, limite_pecas)
            eu_joguei = True
    print("Fim de jogo!! Você ganhou" if eu_joguei else "Fim de jogo!! O computador ganhou!")


def campeonato():
    rodada = 1
    minhas_vitorias = 0
    vitorias_pc = 0
    print("Você escolheu um campeonato!")
    print()
    while rodada <= 3:
        print("**** Rodada ", rodada, " ****")
        print()
        quant_pecas = int(input("Quantas peças? "))
        limite_pecas = int(input("Limite de peças por jogada? "))
        bad_value = True
        if (limite_pecas > 0):
            bad_value = False
        while bad_value:
            limite_pecas = int(input("Limite de peças por jogada? "))
            if (limite_pecas > 0):
                bad_value = False
        if (quant_pecas % (limite_pecas + 1) == 0):
            print("Você começa")
            print()
            quant_pecas = quant_pecas - usuario_escolhe_jogada(quant_pecas, limite_pecas)
            eu_joguei = True
        else:
            print("Computador começa")
            print()
            quant_pecas = quant_pecas - computador_escolhe_jogada(quant_pecas, limite_pecas)
            eu_joguei = False
        while quant_pecas > 0:
            if (quant_pecas == 1):
                print("Agora resta apenas uma peça no tabuleiro")
            else:
                print("Agora restam", quant_pecas, "peças no tabuleiro")
            if (eu_joguei):
                quant_pecas = quant_pecas - computador_escolhe_jogada(quant_pecas, limite_pecas)
                eu_joguei = False
            else:
                quant_pecas = quant_pecas - usuario_escolhe_jogada(quant_pecas, limite_pecas)
                eu_joguei = True
        if (eu_joguei):
            print("Fim de Jogo!! Você ganhou!")
            minhas_vitorias += 1
        else:
            print("Fim de Jogo!! O computador ganhou")
            vitorias_pc += 1
        rodada += 1
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você ", minhas_vitorias, " X ", vitorias_pc, " Computador")


def print_options():
    option = int(input("""Bem-vindo ao jogo do NIM! Escolha:
1 - para jogar uma partida isolada
2 - para jogar campeonato """))
    return option


def main():

    opção = print_options()
    while opção != 1 or opção != 2:
        print()
        print("Opps!! Digite uma opção válida")
        print()
        print_options()
    if opção == 1:
        partida()
    else:
        campeonato()

main()
