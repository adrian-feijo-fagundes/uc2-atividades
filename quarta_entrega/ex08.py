import json

def salvarTarefas(tarefas):
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregarTarefas():
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

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
    salvarTarefas(tarefas)
    print("Tarefa adicionada com sucesso")

def deleteTarefa(tarefas):
    listarTarefas(tarefas)
    exc = int(input("Qual tarefa deseja excluir?")) - 1
    if exc < len(tarefas) and exc >= 0:
        tarefas.pop(exc)
        salvarTarefas(tarefas)
        print("Tarefa excluída com sucesso")
    else:
        print("Valor inválido")

def quantidadeTarefas(tarefas):
    print(f"Atualmente existem {len(tarefas)} tarefas na lista.") 

tarefas = carregarTarefas()

while True:
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Mostrar quantidade de tarefas")
    print("0 - Sair\n")

    opt = int(input("Escolha uma opção: "))

    match opt: 
        case 0:
            print("Saindo do programa")
            break 
        case 1:
            createTarefa(tarefas)
        case 2:
            listarTarefas(tarefas)
        case 3:
            deleteTarefa(tarefas)
        case 4:
            quantidadeTarefas(tarefas)
        case _: 
            print("Opção inválida") 
    
    input("\nDigite enter para continuar...")
    print("\033[2J\033[H", end="")