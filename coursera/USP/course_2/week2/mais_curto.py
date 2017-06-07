def menor_nome(lista_nomes):
    nome_mais_curto = lista_nomes[0].strip()
    for nome in lista_nomes:
        if len(nome_mais_curto) > len(nome.strip()):
            nome_mais_curto = nome.strip()

    return nome_mais_curto.capitalize()

lista = ['maria', 'josé', 'PAULO', 'Catarina']

menor_nome(lista)

