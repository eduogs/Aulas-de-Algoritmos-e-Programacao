#aula 04/11

catalogo = [
    {"pessoa": 1, "tipo": "ectomorfo", "peso": 80.6},
    {"pessoa": 2, "tipo": "mesomorfo", "peso": 87.2},
]

proximo_codigo = 3
print(len(catalogo)), "tipo"
print()
print(catalogo[0]["tipo"])

tipo = ("Tipo:")
peso = float(input("Peso: "))
novo = {"pessoa": proximo_codigo, "tipo": tipo, "peso": peso}
catalogo.append += 1
print("Cadastrado", tipo ) 

codigo = int(input("Codigo: "))
encontrado = None
for item in catalogo:
    if item["pessoa"] == codigo:
        break
    if encontrado:
        print(encontrado["pessoa"],)