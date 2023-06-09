def calcular_fatorial(n):
    if n < 0:
        raise ValueError("Negative values are not alowed")
    if n < 2:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

def calcular_media(lista):
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia.")
    return sum(lista) / len(lista)

def verificar_palindrome(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]
