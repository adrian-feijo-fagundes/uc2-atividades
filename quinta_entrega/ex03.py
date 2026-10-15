while True:
    print("1 - Mostrar uma dica sobre Python")
    print("2 - Mostrar uma dica sobre inteligência artificial")
    print("3 - Mostrar uma mensagem de incentivo")
    print("0 - Sair")
    opt = input("\nEscolha uma opção ").strip().lower()
    match opt:
        case "1": 
            print("Dica Python: use `len()` para descobrir o tamanho de uma lista ou de um texto.")
        case "2":
            print("Dica IA: modelos aprendem padrões a partir de dados.")
        case "3":
            print("Continue praticando! Cada erro é uma oportunidade de aprender.") 
        case "0":
            print("Saindo do programa")
            break 
        case _:
            print("Comando desconhecido") 