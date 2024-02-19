# Ex.003

primeiro_valor = int(input("Digite o 'Primeiro' valor: "))
segundo_valor = int(input("Digite o 'Segundo' valor: "))

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} é maior que o {segundo_valor=}")
elif segundo_valor > primeiro_valor:
    print(f"{segundo_valor=} é maior que o {primeiro_valor=}")
else: 
    print(f"o {primeiro_valor=} é igual ao {segundo_valor=}")