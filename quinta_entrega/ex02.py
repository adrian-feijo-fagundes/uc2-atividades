while True:
    opt = input("Digite: ").strip().lower()
    match opt:
        case "oi" | "olá": 
            print("Olá que bom te ver aqui!") 
        case "ajuda" | "?": 
            print("comandos disponíveis") 
            print("( oi ou olá )") 
            print("( ajuda ou ? )") 
            print("( sair ou 0") 
        case "sair" | "0":
            print("Saindo do programa")
            break 
        case _:
            print("Comando desconhecido") 