confiancas = [0.95, 0.65, 0.34, 0.82, 0.71]


for confianca in confiancas:
    if confianca >= 0.8:
        print(f"{confianca} Alta confiança")
    elif confianca >= 0.5:
        print(f"{confianca} Confiança média")
    else:
        print(f"{confianca} Baica confiança")
