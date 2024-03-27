from array import array

# Array (Matriz)
    # Similar a Listas
    # Melhor Performance

letras_u = ["a", "b", "c", "d"]
numero_i = [10, 20, 30,40]
numero_f = [1.2, 2.2, 3.2]

print(letras_u)
print(numero_i)
print(numero_f)
print()

letras_u = array("u", letras_u)
numero_i = array("i", numero_i)
numero_f = array("f", numero_f)

print(letras_u)
print(numero_i)
print(numero_f)