idade = int(input("Digite a sua 'idade': "))

if idade < 13:
    print("Você é uma 'Criança'")
elif idade > 13 and idade < 18:
    print("Você é um 'Adolescente'")
else:
    print("Você é um 'Adulto'")
