country = {
    "Brasil": "BR",
    "Colombia": "CO",
    "Chile": "CL",
    "Paraguai": "PY",
    "Peru": "PE",
    "Uruguai": "UY",
    "Venezuela": "VE",
    "Argentina": "AR"
}

countryUser = input("Digite o nome do seu 'país': ")

if countryUser in country:
    print(f"O seu 'país' é: {country[countryUser]}")
else:
    print("País Inexistente")
