# Listas
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável


produtos = ["Mouse", "Teclado", "Monitor", "Cadeira", "Fone de Ouvido", "Mousepad"]

item1, item2, item3, *outros = produtos
item1, *outros, item3 = produtos

print(item1, item2, item3)
print(outros)