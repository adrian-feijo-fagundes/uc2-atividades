def contar_classificacao(previsoes, categoria):
    qtd = 0
    for item in previsoes:
        if item == categoria:
            qtd += 1
    return qtd



previsoes = ["gato", "cachorro", "gato", "pássaro", "gato"]
print(contar_classificacao(previsoes, "gato"))
print(contar_classificacao(previsoes, "cachorro"))
print(contar_classificacao(previsoes, "passaro"))