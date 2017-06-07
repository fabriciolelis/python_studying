def conta_letras(frase, contar='vogais'):
    vogais_lista = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vogais = 0
    consoantes = 0
    for c in frase.replace(' ',''):
        if c in vogais_lista:
            vogais += 1
        else:
            consoantes += 1
    return consoantes if contar == 'consoantes' else vogais


frase = 'programamos em python'

print(conta_letras(frase))
