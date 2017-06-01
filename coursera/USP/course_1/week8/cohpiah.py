import re
import math

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def converte_matriz_em_lista(matriz):
    lista = []
    linhas = len(matriz)
    for i in range(linhas):
        colunas = len(matriz[i])
        for j in range(colunas):
            lista.append(matriz[i][j])
    return lista

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    tamanho = len(as_a)
    i = 0
    similaridade = 0
    somatorio = 0
    while i < tamanho:
        somatorio = somatorio + math.fabs(as_a[i] - as_b[i])
        i = i + 1
    similaridade = somatorio / tamanho
    return similaridade


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases_matriz = []
    total_caracteres_sen = 0

    for sentenca in sentencas:
        frases_matriz.append(separa_frases(sentenca))
        total_caracteres_sen =  total_caracteres_sen + len(sentenca)
    frases = converte_matriz_em_lista(frases_matriz)
    tamanho_medio_sentenca = total_caracteres_sen / len(sentencas)

    palavras_matriz = []
    total_carc_frases = 0
    for frase in frases:
        palavras_matriz.append(separa_palavras(frase))
        total_carc_frases = total_carc_frases + len(frase)
    palavras = converte_matriz_em_lista(palavras_matriz)
    tamanho_medio_frase = total_carc_frases / len(frases)

    tamanho_palavras = 0
    total_palavras = len(palavras)
    total_palavras_dif = n_palavras_diferentes(palavras)
    total_palavras_unica = n_palavras_unicas(palavras)

    for palavra in palavras:
        tamanho_palavras = tamanho_palavras + len(palavra)
    tamanho_medio_palavras = tamanho_palavras / total_palavras

    typeToken = total_palavras_dif / total_palavras
    hapaxLegomana = total_palavras_unica / total_palavras
    complexidade = len(frases) / len(sentencas)

    return [tamanho_medio_palavras, typeToken, hapaxLegomana, tamanho_medio_sentenca, complexidade, tamanho_medio_frase]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (0 a n-1)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    calculos_ass = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))
    for assinatura in assinaturas:
        calculos_ass.append(compara_assinatura(assinatura, ass_cp))
    indice = calculos_ass.index(min(calculos_ass))
    print("O autor do texto", indice + 1, "está infectado com COH-PIAH")
    return indice

assinatura_cp = le_assinatura()
textos_lidos = le_textos()
avalia_textos(textos_lidos, assinatura_cp)
