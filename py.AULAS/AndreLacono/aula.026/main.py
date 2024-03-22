# While Loop

valor = int(input("Digite o valor do seu produto: "))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f"O valor do seu produto é: {valor}")
    break;

x = True

while x:
    for i in (range(10)):
        if (i == 5):
            x = False