# Lambda Function 
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos mas somente e 1 expressão
    # Muito utilizada dentro de outras funções
    # Código mais 'clean'

def somar(x):
    resultado = lambda x: x + 10
    return resultado(x) * 4

print(somar(2))