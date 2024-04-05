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
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

user1 = Pessoa("Elena", "Santos", 2003)
user2 = Pessoa("Lutek", "Dev", 2003)

print(user2.nome)