temperature = int(input("Qual é a temperatura da carne? "))

if temperature < 48:
    print("Cozinhar por mais alguns minutos")
elif temperature >= 48 and temperature < 54:
    print("Selada")
elif temperature >= 54 and temperature < 60:
    print("Ao ponto para o mal")
elif temperature >= 60 and temperature < 65:
    print("Ao Ponto")
elif temperature >= 65 and temperature < 71:
    print("Ao ponto para o bem")
else:
    print("Bem Passada")
