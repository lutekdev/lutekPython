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

from datetime import datetime

class Pessoa:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento
    
    def nome_completo(self):
        return self.nome + " " + self.sobrenome

    def idade_pessoa(self):
        ano_atual = datetime.now().year
        return ano_atual - self.data_nascimento  

user1 = Pessoa("Elena", "Santos", 1990)
user2 = Pessoa("Lutek", "Dev", 2003)

# print(f"Meu nome é {user1.nome} {user1.sobrenome}, tenho {user1.data_nascimento - 2003} anos")
print(user1.nome_completo())
print(user2.nome_completo())
print(Pessoa.nome_completo(user1))
print(Pessoa.nome_completo(user2))

print(Pessoa.idade_pessoa(user1))
print(Pessoa.idade_pessoa(user2))