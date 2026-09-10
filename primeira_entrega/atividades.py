from datetime import datetime
from formatador import colorir 


############################################################################
print(colorir("\n   Exercício 01 — Apresentação \n", cor="verde"))

print("Olá.")
print("Meu nome é Adrian.")
print("Estou aprendendo Python.")

############################################################################
print(colorir("\n   Exercício 02 — sep \n", cor="verde"))

print("Senac", "TIA", "Python é legal", sep=" | ")

############################################################################
print(colorir(f"\n   Exercício 03 — Data Atual \n", cor="verde"))

data = datetime.now()
print(str(data.day).zfill(2), end="/")
print(str(data.month).zfill(2), end="/")
print(str(data.year).zfill(2))

############################################################################
print(colorir(f"\n   Exercício 04 — end \n", cor="verde"))

print("Python é", end=" ")
print("muito", end=" ")
print("legal")

############################################################################
print(colorir(f"\n   Exercício 05 — Criando variáveis \n", cor="verde"))

nome = "Adrian"
idade = 23
cidade = "São Leopoldo"
curso = "Técnico em Inteligência Artificial"

print(f"Meu nome é {nome}, tenho {idade} anos,", sep=" ")
print(f"moro em {cidade} e faço o curso de {curso}.")

############################################################################
print(colorir(f"\n   Exercício 06 — Tipos de dados \n", cor="verde"))

nome = "Adrian Feijó Fagundes"
idade = 23
altura = 1.8
matriculado = True

print("Tipo da variável nome:", type(nome))
print("Tipo da variável idade:", type(idade))
print("Tipo da variável altura:", type(altura))
print("Tipo da variável maticulado:", type(matriculado))

############################################################################
print(colorir(f"\n   Exercício 07 — Personagem \n", cor="verde"))

nome = "Aragorn"
classe = "Guerreiro"
nivel = 10
possui_equipamento = True

print("===== PERSONAGEM =====")
print("Nome: ", nome)
print("Classe: ", classe)
print("Nível: ", nivel)
print("Possui equipamento: ", possui_equipamento)

############################################################################
print(colorir(f"\n   Exercício 08 — Entrada de dados \n", cor="verde"))

nome = ""
cidade = ""

nome          = input("Qual é o seu nome? ")
cidade        = input("Qual é a sua cidade? ")
jogo_favorito = input("Qual é o seu jogo favorito? ")

print(f"\nOlá, {nome}! Você mora em {cidade} e seu jogo favorito é {jogo_favorito}.")

############################################################################
print(colorir(f"\n   Exercício 09 — Curso \n", cor="verde"))

curso = ""

aluno = input("Qual o nome do aluno? ")
curso = input("Qual o curso? ")
unidade = input("Qual a unidade? ")
turno = input("Qual turno do curso? ")

print("===== MATRÍCULA =====\n")
print("Aluno:", aluno)
print("Curso:", curso)
print("Unidade:", unidade)
print("Turno:", turno)
