nota = float(input("Digite sua nota: "))
frequencia = float(input("Digite sua frêquencia: "))
situacao = "Reprovado"

if frequencia >= 75:
    if nota >= 7:
       situacao = "Aprovado"
    elif nota >= 5:
       situacao = "Recuperação"
    print(situacao)
else:
    print(situacao, "por frequência")