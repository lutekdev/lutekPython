# Lambda Function 
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos mas somente e 1 expressão
    # Muito utilizada dentro de outras funções
    # Código mais 'clean'

# def somar(x):
#     return x + 10

# somar10 = lambda x : x + 10
somar10 = lambda x, y : x + y + 10
print(somar10(2, 4))