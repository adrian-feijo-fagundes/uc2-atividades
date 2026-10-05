previsoes = [
    "gato",
    "cachorro",
    "gato",
    "gato",
    "cachorro",
    "pássaro",
    "gato"
]

contagem = {}

for animal in previsoes:
    if animal in contagem:
        contagem[animal] += 1
    else:
        contagem[animal] = 1

for animal, quantidade in contagem.items():
    print(f"{animal}: {quantidade}")