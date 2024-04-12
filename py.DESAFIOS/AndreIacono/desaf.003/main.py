func = {"Ana", "Marcos", "Alice", "Pedro", "Sophia", "Bruno", "Melissa"}
turn_dia = {"Ana", "Marcos", "Alice", "Melissa"}
turn_noite = {"Pedro", "Sophia", "Bruno"}
tem_carro = {"Marcos", "Alice", "Bruno", "Melissa"}

list1 = func.intersection(tem_carro) and turn_noite.intersection(tem_carro)
list2 = func.intersection(tem_carro) and turn_dia.intersection(tem_carro)
list3 = func.symmetric_difference(tem_carro)

print(f"Lista 1: {list1}")
print(f"Lista 2: {list2}")
print(f"Lista 3: {list3}")
