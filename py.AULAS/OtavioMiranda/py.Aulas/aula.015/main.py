# IF / Elif / Else
# Se / Se Não Se / Se Não

entrada = input("Você quer 'entrar' ou 'sair': ")

if entrada == "entrar" or entrada == "Entrar":
    print('Você entrou no Sistema!')
elif entrada == "sair" or entrada == "Sair":
    print('Você saiu do Sistema!')
else:
    print("Você não escolheu nenhuma opção.")