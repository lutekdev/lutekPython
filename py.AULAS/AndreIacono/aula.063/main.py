# Erros
    # Excelente para testes
    # Não Realiza o "Stop" No Programa
    # Mensagens Customizadas Quando Encontra o Erro

try:
    valor = int(input("Digite o valor do seu produto: "))
    print(f"O valor do seu produto é: {valor}")
except ValueError:
    print("Erro ao digitar o valor do seu produto")
else:
    print("Obrigado por digitar o valor do seu produto")
    print(f"Seu Produto Com 10% de Desconto é: {valor * 0.10 + valor}")
finally:
    print("Code Download")
