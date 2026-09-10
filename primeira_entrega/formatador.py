def colorir(texto, cor="reset"):
    # Dicionário com os códigos de cores
    cores = {
        "preto": "30",
        "vermelho": "31",
        "verde": "32",
        "amarelo": "33",
        "azul": "34",
        "magenta": "35",
        "ciano": "36",
        "branco": "37",
        "reset": "0"
    }
    
    # Pega o código da cor (se não existir, usa o reset)
    codigo_cor = cores.get(cor.lower(), "0")
           
    prefixo = f"\033[{';'.join(codigo_cor)}m"
    sufixo = "\033[0m"
    
    return f"{prefixo}{texto}{sufixo}"