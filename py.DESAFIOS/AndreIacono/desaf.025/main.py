cidadesSets = {"Belo Horizonte", "São Paulo", "Rio de Janeiro", "Porto Alegre"}

userCity = input("Digite uma Cidade: ")

if userCity in cidadesSets:
    print("A Cidade está na lista de cidades;")
else:
    print("A cidade não está na lista de cidades;")
