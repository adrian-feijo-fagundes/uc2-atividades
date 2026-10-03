previsoes = [
    0.92,
    0.84,
    0.35,
    0.76,
    0.28,
    0.95
]


for previsao in previsoes:
    if previsao < 0.30:
        print(f"Confiança muito pequena {previsao}")
        break
    print(f"Confiança {previsao}")
