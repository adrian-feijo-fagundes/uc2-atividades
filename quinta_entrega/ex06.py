resultados = [
    "positivo",
    "negativo",
    "positivo", 
    "neutro", 
    "erro", 
    "negativo"
]
positivos = 0
negativos = 0
neutros = 0
desconhecidos = 0

for valor in resultados:
    match valor:
        case "positivos":
            positivos += 1
        case "negativos":
            negativos += 1
        case "neutros":
            neutros += 1
        case "desconhecidos":
            desconhecidos += 1            

