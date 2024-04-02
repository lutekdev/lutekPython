# Tuples
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em um variável
    # Não podem ser alteradas
    # Se Os Itens não forem alterados então use Tuples (Rápido, Leve e não usa muita memoria)

produtos_list = ["Mouse", "Teclado", "Monitor", "Cadeira", "Fone de Ouvido", "Mousepad"]
produtos_tuple = ("Mouse", "Teclado", "Monitor", "Cadeira", "Fone de Ouvido", "Mousepad")

# print(type (produtos_list))
# print(type(produtos_tuple))

print(produtos_list)
print(produtos_tuple)

duas_list = produtos_tuple * 2

print(duas_list)