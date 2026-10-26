def calcular_media(notas):
    if notas == []:
        return None

    soma = sum(notas)
    if soma == 0:
        return 0

    return soma / len(notas)

def exibe_resultado(resultado):
    if resultado is None:
        print("O resultado não foi calculado, é None")
    else:
        print(f"O resultado é: {resultado}")


notas = [8.0, 6.0, 10.0]
exibe_resultado(calcular_media(notas))
notas = [0.0, 0.0]
exibe_resultado(calcular_media(notas))
notas = []
exibe_resultado(calcular_media(notas))
