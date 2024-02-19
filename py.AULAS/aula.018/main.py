entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")
senha_permitida = "123"

if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrar")
elif entrada == "S":
    print("Sair")
elif entrada != "E" and entrada != "S":
    print("Opção Invalida")
else:
    print("Senha Invalida")