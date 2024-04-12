type = input("Digite o Tipo de Operação: ")
num1 = input("Digite o Primeiro Número: ")
num2 = input("Digite o Segundo Número: ")

if type == "+":
    print(f"O Resultado da Soma é: {int(num1) + int(num2)}")
elif type == "-":
    print(f"O Resultado da Subtração é: {int(num1) - int(num2)}")
elif type == "*":
    print(f"O Resultado da Multiplicação é: {int(num1) * int(num2)}")
elif type == "/":
    resultado = float(num1) / float(num2)
    print(f"O Resultado da Divisão é: {resultado:.2f}")
elif type == "**":
    print(f"O Resultado da Potência é: {int(num1) ** int(num2)}")
