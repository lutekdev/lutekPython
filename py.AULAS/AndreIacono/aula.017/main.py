# Logical Operators (Operadores Lógicos)

renda = input("Digite sua renda: ")
renda = float(renda)
nome_limpo = input("Digite se seu nome está limpo: ")

if nome_limpo == "sim" or nome_limpo == "Sim":
    if renda > 5000:
        print("Financiamento Aprovado!!")
    else:
        print("Financiamento Reprovado!!")
else:
    print("Financiamento Reprovado!!")