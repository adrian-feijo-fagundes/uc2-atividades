notas = [7.5, 8.0, 5.5, 9.0, 6.5]

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

while True:
    print("1 - Listar notas")
    print("2 - Mostrar média")
    print("3 - Mostrar maior nota")
    print("4 - Mostrar menor nota")
    print("0 - Sair")
    opt = input("\nEscolha uma opção: ").strip().lower()
    match opt:
        case "1": 
            print("notas da lista:")
            for nota in notas:
                print(notas)
        case "2":
            print(f"A média das notas é {media}")
        case "3":
            print(f"A maior nota é {maior}")
        case "4":
            print(f"A menor nota é {menor}")
        case "0" | "sair":
            print("Saindo do programa")
            break
    input("Digite enter para continuar...")