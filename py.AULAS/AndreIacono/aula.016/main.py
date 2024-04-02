velocidade = input("Digite a Velocidade: ")
velocidade = int(velocidade)

if velocidade > 110:
    print("Velocidade Acima do Permitido!")
elif velocidade < 60:
    print("Favor dirigir acima de 80Km/h")    
else:
    print("Velocidade Permitida")