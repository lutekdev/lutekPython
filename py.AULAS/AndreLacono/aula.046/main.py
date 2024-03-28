# Set (Listas)
    # Similar a Listas
    # Evita itens duplicados
    # Não utiliza index

list1 = [10,20, 30, 40, 50]
list2 = [10, 20, 60]

num1 = set(list1)
num2 = set(list2)

# Union (União) (Juntar os itens de num1 e num2 sem duplicidade)
print(num1 | num2) 

# Difference (Diferença) (Pega os valores que não são repetidos entre num1 e num2)
print(num1 - num2) 

# Symmetric Difference (Diferença Simétrica) (Pega os valores que não são repetidos entre num1 e num2) 
print(num1 ^ num2) 

# Intersection (Intersecção) (Pega os itens que são repetidos entre num1 e num2)
print(num1 & num2) 

# Length (Tamanho) (Quantidade de itens)
print(len(num1))