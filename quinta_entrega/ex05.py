compras = []

while True:
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Remover produto pelo nome")
    print("4 - Mostrar quantidade de produtos")
    print("0 - Sair")
    opt = input("\nEscolha uma opção: ").strip().lower()
    match opt:
        case "1": 
            produto = input("Digite o nome do produto: ").strip()
            if not produto:
                print("Nome do produto vazio")
                continue
            compras.append(produto)
        case "2":
            if len(compras) != 0:
                print("lista de compras:")
                for produto in compras:
                    print(f"- {produto}")
            else:
                print("Ainda não adicionou nada a lista!")
        case "3":
            produto = input("Digite o nome de um produto para remover").strip().lower()
            if produto in compras:
                compras.remove(produto)
            else:
                print("Produto não encontrado")    
        case "4":
            print(f"A quantidade de produtos cadastrados é {len(compras)}")
        case "0" | "sair":
            print("Saindo do programa")
            break 
    input("Digite enter para continuar...")