# Generator Expressions
    # Uma forma mais rápida para Listas, Sets e Dicionários
    # Menos memória alocada
    # Valores em Bytes

from sys import getsizeof

numero = [x * 10 for x in range(10000)]
print(getsizeof(numero))

print(10 * "==")
numero = (x * 10 for x in range(10000))
print(getsizeof(numero))

print(getsizeof(list(numero)))