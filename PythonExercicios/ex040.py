nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Com notas {:.1f} e {:1.f}, a média é {:.1f}.'.format(nota1, nota2, media))
if media < 5.0:
    print('O aluno está REPROVADO!!')
elif 5.0 <= media < 7.0:
    print('O aluno está em RECUPERAÇÃO!!')
else:
    print('O aluno está APROVADO!!')

