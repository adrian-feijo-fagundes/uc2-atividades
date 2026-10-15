alunos = []

while True:
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Mostrar quantidade de aluno")
    print("0 - Sair")
    opt = input("\nEscolha uma opção ").strip().lower()
    match opt:
        case "1": 
            aluno = input("Digite o nome do aluno: ")
            if not aluno:
                print("Nome vazio")
                continue
            alunos.append(aluno)
        case "2":
            print("lista de alunos:")
            for aluno in alunos:
                print(aluno)
        case "3":
            print(f"A quantidade de alunos cadastrados é {len(alunos)}")
        case "0":
            print("Saindo do programa")
            break 
    input("Digite enter para continuar...")



