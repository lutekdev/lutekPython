listCar = ["BMW X6", "BMW i5", "BMW i8"]

chooserUser = input("Digite o nome do carro que deseja comprar: ")

if chooserUser in listCar:
    print(f"O Carro {chooserUser} está disponível!")
else:
    print(f"Desculpe, este carro {chooserUser}, não está disponível!")
