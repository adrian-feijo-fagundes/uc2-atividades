def contar(lista, literal):
    qtd = 0
    for item in lista:
        if item == literal:
            qtd += 1
    return qtd

previsoes = []
opcoes_validas = ["gato","cachorro","passaro"]

while True:
    print("1 - Adicionar classificação")
    print("2 - Listar classificações")
    print("3 - Mostrar quantidade de gatos")
    print("4 - Mostrar quantidade de cachorros")
    print("5 - Mostrar total de classificações")
    print("0 - Sair")
    opt = input("\nEscolha uma opção: ").strip().lower()
    match opt:
        case "1": 
            classificacao = input("\nEscreva uma classificação: ").strip().lower()
            if classificacao not in opcoes_validas:
                print("Opção inválida são permitidas apenas gato, cachorro ou passaro")
                continue
            previsoes.append(classificacao)
        case "2":
            if previsoes == []:
                print("A lista está vazia.")
            else:
                print("Lista de classificações:")
                for item in previsoes:
                    print(f"- {item}") 
        case "3":
            print(f"A quantidade de gatos na lista é {contar(previsoes, "gato")}")
        case "4":
            print(f"A quantidade de cachorros na lista é {contar(previsoes, "cachorro")}")
        case "5":
            if previsoes == []:
                print("Não tem nenhuma classificação")
            else:
                print(f"A quantidade total de classificações é {len(previsoes)} ")
        case "0" | "sair":
            print("Saindo do programa")
            break
    input("Digite enter para continuar...")