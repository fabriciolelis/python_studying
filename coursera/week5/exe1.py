def fizzbuzz(inteiro):
    if (inteiro % 3 == 0) and (inteiro % 5 == 0):
        return "FizzBuzz"
    elif (inteiro % 5 == 0):
        return "Buzz"
    elif (inteiro % 3 == 0):
        return "Fizz"
    else:
        return inteiro


inteiro = int(input("Digite um inteiro: "))
print(fizzbuzz(inteiro))
