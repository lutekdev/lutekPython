frutaUser = input("Digite uma fruta: ")

while frutaUser.lower() != "abacate":
    frutaUser = input("Fruta Invalida. Digite uma fruta: ")

    if frutaUser.lower() == "abacate":
        print("Parabéns, você acertou a fruta!")
        break
