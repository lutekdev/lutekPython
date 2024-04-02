cor_clientes = input("Digite a cor desejada: ")
cores = ["amarelo", "verde", "azul", "vermelho"]

if cor_clientes.lower() in cores :
    print("Em Estoque")
else:
    print("Não temos está cor em estoque")