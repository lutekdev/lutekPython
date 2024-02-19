senha_digitada = input("Senha: ")
senha_permitida = "123"

if not senha_digitada:
    print("Você não digitou a senha.")
elif senha_digitada == senha_permitida:
    print("Acesso permitido")
else:
    print("Acesso negado")