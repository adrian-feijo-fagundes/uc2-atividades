previsoes = [
    "gato",
    "cachorro",
    "gato",
    "pássaro",
    "gato",
    "cachorro"
]
qtd_gatos = 0
for previsao in previsoes:
    if previsao == "gato":
        qtd_gatos += 1

print(f"Gatos detectados: {qtd_gatos}")