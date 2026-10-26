from cria_menu import cria_menu

alunos = []

def pede_nome():
    nome = input("Qual o nome do aluno: ").strip().lower()
    return nome

def tem_alunos(alunos):
    return len(alunos) != 0

def listar_alunos(alunos):
    if not tem_alunos(alunos):
        print("Não tem nenhum aluno cadastrado")
        return
    
    print("Alunos cadastrados:")
    for aluno in alunos:
        print(f"- {aluno}")

def buscar_aluno(alunos, nome):
    return nome in alunos
        
def remover_aluno(alunos, nome):
    if buscar_aluno(alunos, nome):
        alunos.remove(nome)
        return True
    return False

def cadastrar_aluno(alunos, nome):
    if nome != "" and not buscar_aluno(alunos, nome):
        alunos.append(nome)
        return True
    return False


def opc_cadastrar_aluno():
    nome = pede_nome()
    if cadastrar_aluno(alunos, nome):
        print("Aluno cadastrado com sucesso")
        return
    print("Não foi possível cadastrar o aluno, verifique se é um nome válido")

def opc_listar_alunos():
    listar_alunos(alunos)

def opc_buscar_aluno():
    nome = pede_nome()
    buscar_aluno(alunos, nome)

def opc_buscar_aluno():
    listar_alunos(alunos)
    print("Aluno a remover")
    nome = pede_nome()
    if remover_aluno(alunos, nome):
        print(f"O aluno {nome} foi removido com sucesso")
        return
    print("Aluno não estava cadastrado")

def opc_mostrar_quantidade_alunos():
    if tem_alunos(alunos):
        print(f"Atualmente existem {len(alunos)} cadastrados.")
    else:
        print("Nenhum aluno cadastrado")

lista = [
    ("Cadastrar aluno", opc_cadastrar_aluno),
    ("Listar alunos", opc_listar_alunos),
    ("Buscar aluno", opc_buscar_aluno),
    ("Remover aluno", opc_buscar_aluno),
    ("Mostrar quantidade de alunos", opc_mostrar_quantidade_alunos),
]

cria_menu(lista)