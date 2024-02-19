entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ")
senha_permitida = "123"

if (entrada == "E" or entrada == "e") and (senha_digitada == senha_permitida):
    print("Entrar")
elif (entrada == "S" or entrada == "s") and (senha_digitada == senha_permitida):
    print("Sair")
elif (entrada != "E" or entrada != "e") and (entrada != "S" or entrada != "s"):
    print("Opção Invalida")
else:
    print("Senha Invalida")