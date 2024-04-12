# Calculadora de IMC - Índice de Massa Corporal

altura = float(input("Qual é a sua 'Altura' em cm: "))
peso = float(input("Qual é o seu 'Peso' em kg: "))
resultado = float(peso / (altura) ** 2)

if resultado == 18.5:
    print(f"Seu 'Peso' equivale: {resultado:.2f}")
    print("Resultado = 'Magreza'")
elif resultado > 18.5 and resultado < 24.9:
    print(f"Seu 'Peso' equivale = {resultado:.2f}")
    print("Resultado = 'Normal'")
elif resultado > 24.9 and resultado < 29.9:
    print(f"Seu 'Peso' equivale = {resultado:.2f}")
    print("Resultado = 'Sobrepeso'")
elif resultado > 29.9 and resultado < 34.9:
    print(f"Seu 'Peso' equivale = {resultado:.2f}")
    print("Resultado = 'Obesidade Grau I'")
elif resultado > 34.9 and resultado < 39.9:
    print(f"Seu 'Peso' equivale = {resultado:.2f}")
    print("Resultado = 'Obesidade Grau II'")
else:
    print(f"Seu 'Peso' equivale =  {resultado:.2f}")
    print("Resultado = 'Obesidade Grau III'")
