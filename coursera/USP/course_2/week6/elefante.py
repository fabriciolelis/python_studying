def incomodam(n):
    if n < 1:
        return ""
    else:
        return "incomodam " + incomodam(n - 1)


def incomodam_parte1(n):
    if n == 1:
        return "Um elefante incomoda muita gente"
    else:
        return str(n) + " elefantes " + incomodam(n) + "muito mais"


def incomodam_parte2(n):
    if n <= 1:
        return ""
    else:
        return str(n) + " elefantes " + incomodam(n) + " muita gente"


def elefantes(n):
    if n < 1:
        return ""
    else:
        return elefantes(n - 1) + "\n" + incomodam_parte1(n) + "\n" + incomodam_parte2(n)

print(elefantes(2))
