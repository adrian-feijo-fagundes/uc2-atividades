imagem = [
    [0, 255, 0],
    [255, 255, 0],
    [0, 0, 255]
]

linha = ""

for i in imagem:
    for j in i:
        linha += f" {j}"
    print(linha)
    linha = ""