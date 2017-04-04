from week4.exe5 import primo


def maior_primo(inteiro):
    n = 2
    primo = True
    while n < inteiro and primo:
        if inteiro % n == 0:
            primo = False
    n += 1
print("primo" if primo else "não primo")
# if(primo):
#     print("primo")
# else:
#     print("não primo")

inteiro = int(input("Digite o valor de inteiro: "))
maior_primo(inteiro)
