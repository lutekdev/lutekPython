# def soma(*numbers):
#     return sum(numbers)

def soma1(*numbers):
    resultado = 2

    for num in numbers:
        resultado *= num
    return resultado

# print(f"{soma(10, 20, 30, 40)}")
print(soma1(10, 20, 30, 40))