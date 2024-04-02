# Set (Listas)
    # Similar a Listas
    # Evita itens duplicados
    # Não utiliza index

# list = set([10, 20, 30, 40, 50])
s1 = {10, 20, 30, 40, 50} # Sets
# s2 = {} # Dicionários

s1.add(7)
s1.update([11, 12, 13, 14, 15])
s1.remove(50)
s1.discard(30)

print(s1)