def agencia(**carro):
    return carro


x = agencia(marca="Gol", cor="Branca", motor=1.0, ano=2010)

print(x["motor"])