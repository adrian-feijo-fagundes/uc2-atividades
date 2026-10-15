dia = input("Digite um número de 1 a 7: ").strip().lower()

match dia:
    case "1":
        print("Segunda-feira")
    case "2":
        print("Terça-feira")
    case "3":
        print("Quarta-feira")
    case "4":
        print("Quinta-feira")
    case "5":
        print("Sexta-feira")
    case "6":
        print("Sabádo")
    case "7":
        print("Domingo")
    case _:
        print("Dia inválido.")