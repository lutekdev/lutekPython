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
    nome = "Lutek"
    sobrenome = "Dev"
    year = 2024

user1 = Pessoa()

print(f"Meu nome é {user1.nome}{user1.sobrenome}, tenho {user1.year - 2003} anos")