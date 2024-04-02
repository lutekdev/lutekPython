# Sets (Listas)
    # Similar a Listas
    # Evita itens duplicados
    # Não utiliza index


set1 = {'a', "b", "c"}
set2 = {'b', "a", "c"}
set3 = {'c', "b", "a"}


# set4 = set1.union(set2)
# set4 = set1.difference(set1)
# set4 = set1.intersection(set3)
set4 = set1.symmetric_difference(set3)

print(set4)
