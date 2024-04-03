# Map Function
    # Muito Utilizada em Lista
    # Aplicar uma função a um Iterable, por item (list, tuple, dic, etc.)

# def multi(x):
#     return x * 2

lista1 = [1,2,3,4]
print(list(map(lambda x: x*2, lista1)))

lista2 = [4, 2, 3, 5]
print(list(map(lambda x: x + 5, lista2)))