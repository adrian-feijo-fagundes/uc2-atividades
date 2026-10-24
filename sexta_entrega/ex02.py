def apresentar_aluno(nome, curso):
    print(f"Olá {nome}, bem vindo ao curso {curso}")

def perguntar():
    nome = input("Digite seu nome: ") 
    curso = input("Digite seu curso: ")
    return nome , curso

apresentar_aluno(*perguntar())
apresentar_aluno(*perguntar())