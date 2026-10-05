objetos = [
    "pessoa",
    "carro",
    "pessoa",
    "bicicleta",
    "carro",
    "pessoa"
]

qtd_pessoas = 0

for objeto in objetos:
    if objeto == "pessoa":
        qtd_pessoas += 1
    print(f"Objeto detectado: {objeto}") 


print(f"Total de pessoas detectadas: {qtd_pessoas}") 