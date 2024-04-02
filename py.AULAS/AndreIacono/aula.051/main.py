# Dicionários
    # Utiliza Index no Formato de Keys e Values
    # Aceita Strings, Integer, Float, Complex e Boolean


aluno = {"nome": "Lutek", "idade": 20, "sobrenome": "Dev"}

print("===" * 5)

for x in aluno:
    print(f"- {x.capitalize()} = {aluno[x]}")

print("===" * 5)

# for keys, values in aluno.items():
#     print(keys, values)