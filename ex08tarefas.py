def listarTarefas(tarefas):
    if temTarefa(tarefas):
        print(f"Tarefas:\n")
        contador = 0
        while contador < len(tarefas):
            print(f"{contador + 1} - {tarefas[contador]}")
            contador += 1

def temTarefa(tarefas):
    if len(tarefas) == 0:
        print(f"\nNenhuma tarefa adicionada ainda")
        return False
    return True

def createTarefa(tarefas):
    tarefa = input("Digite uma tarefa: ") 
    tarefas.append(tarefa)

def deleteTarefa(tarefas):
    listarTarefas(tarefas)
    exc = int(input("Qual tarefa deseja excluir?")) - 1
    if exc < len(tarefas) and exc > 0:
        tarefas.pop(exc)
        print("Tarefa excluída com sucesso")
    else:
        print("Valor inválido")

def quantidadeTarefas(tarefas):
    print(f"Atualmente existem {len(tarefas)} tarefas na lista.") 

tarefas = []

while True:
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Mostrar quantidade de tarefas")
    print("0 - Sair\n")

    opt = int(input("Escolha uma opção: "))

    if opt == 0:
        print("Saindo do programa")
        break 
    elif opt == 1:
        createTarefa(tarefas)
    elif opt == 2:
        listarTarefas(tarefas)
    elif opt == 3:
        deleteTarefa(tarefas)
    elif opt == 4:
        quantidadeTarefas(tarefas)
    else: 
        print("Opção inválida") 
    
    input("\nDigite enter para continuar...")
    print("\033[2J\033[H", end="")