# Erros
    # Excelente para testes
    # Não Realiza o "Stop" No Programa
    # Mensagens Customizadas Quando Encontra o Erro

letras = ["a", "b", "c"]

try:
    print(letras[3])
except IndexError:
    print("- Ocorreu um Erro ao Encontrar o Index")