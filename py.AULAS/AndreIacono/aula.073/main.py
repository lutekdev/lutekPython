from functions import find_index

list1 = ['a', 'b', 'c', 'd', 'e']

try:
    print(find_index(list1, "b"))
except:
    print("- Ocorreu um Erro ao Encontrar o Index")