# Listas
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

numero.extend(letras) # Adicionar
# final = numero + letras # Concatenar
print(numero)

itens = [["Mouse", 10], ["Teclado", 20], ["Monitor", 30]] # Listas dentro de Listas

print(itens[0][0]) # Mouse
print(itens[1][0]) # Teclado