def cliente1(nome): # VOID
    print(f"VOID: Ola {nome} seu pedido foi aceito. Obrigado por comprar conosco. Ate mais")


def cliente2(nome): # RETURN
    return f"Ola {nome} seu pedido foi aceito. Obrigado por comprar conosco. Ate mais"


print(5*"===")
print(f"RETURN: {cliente1("LutekDev")}")
print(5*"===")

print(5*"-X-")

print(5*"===")
print(f"RETURN: {cliente2("LutekDev")}")
print(5*"===")