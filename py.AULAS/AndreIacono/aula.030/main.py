# Functions (Funções)
    # DRY - Don't Repeat Yourself
    # Parâmetro - Argumento
    # Default - Aquele que você define o valor no parâmetro
    # Non-Default - Aquele que você não define o valor no parâmetro

def boas_vindas(nome, pack=5):
    print(f"Olá {nome}")
    print(f"Temos {str(pack)} laptops em estoque")

boas_vindas("Otávio")    
boas_vindas("LutekDev")
