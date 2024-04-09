in_rend = int(input("Qual o rendimento da lata? "))
in_alt = int(input("Qual é a altura da parede? "))
in_lar = int(input("Qual é a largura da parede? "))


def calculo(rend, alt, lar):
    return (alt * lar) / rend


calculoTeste = calculo(in_rend, in_alt, in_lar)

print(f"Você precisa de {calculoTeste:.2f} litros de tinta.")
