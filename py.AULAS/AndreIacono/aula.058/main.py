# List Comprehension
    # Mais Simples de Escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expression for item in list]

frutas1 = ["abacate", "abacaxi", "banana", "morango", "kiwi"]

frutas2 = [item for item in frutas1 if "k" in item]

# for itens in frutas1:
#     if 'n' in itens:
#         frutas2.append(itens)

print(frutas2)