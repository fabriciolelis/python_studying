def maior_primo(inteiro):
    n = 2
    primo = True
    while n < inteiro and primo:
        if inteiro % n == 0:
            primo = False
    n = n + 1

if(primo):
    print("primo")
else:
    print("não primo")

inteiro = int(input("Digite o valor de inteiro: "))
maior_primo(inteiro)
