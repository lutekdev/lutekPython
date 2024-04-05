# Python Object-Oriented Programming

# Classes
    # ========================================================================== #
    # Utilizadas para criar Objetos (instances)
    # Objetos são partes dentro de uma Class (instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    # ========================================================================== #
    # Class: Frutas
    # Objects: Abacate, Banana
    # ========================================================================== #

class Pessoa:
    pass

user1 = Pessoa()

# Criar Parâmetros
user1.nome = "Elena"
user1.sobrenome = "Cabral"
user1.data_nascimento = "12/01/2009"

print(user1.nome)