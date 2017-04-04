inteiro = int(input("Digite o valor de inteiro: "))

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
