def add(a, b):
    """
    Implementar adição usando incrementos
    """
    resultado = a + b
    return resultado

def multiply(a, b):
    """
    Implementar multiplicação como adição repetida
    """
    resultado = 0
    for _ in range(b):
        resultado = add(resultado, a)
    return resultado

def power(base, exponent):
    """
    Implementar potência usando multiplicação repetida
    """
    resultado = 1
    for _ in range(exponent):
        resultado = multiply(resultado, base)
    return resultado

def factorial(n):
    """
    Implementar fatorial (base para probabilidade)
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado = multiply(resultado, i)
    return resultado
    