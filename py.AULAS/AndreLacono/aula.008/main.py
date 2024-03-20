nome = input("Digite seu Nome: ")
idade = input("Digite Sua Idade: ")
ano = input("Em Que Ano você está: ")
anoNascimento = int(ano) - (int(idade) + 1)
workManager = input("Digite sua Profissão: ")

print(f"Seu Nome é {nome} e você tem {idade} anos, e nasceu no ano de {anoNascimento}. Atualmente você esta trabalhando como: {workManager}.")