usuarios = [
    "admin",
    "maria",
    "joao",
    "pedro"
]

nome = input("Digite um nome: ").lower()

contador  = 0
while contador < len(usuarios):
    if usuarios[contador] == nome:
        print("Usuario encontrado")
        break
    contador += 1

if contador == len(usuarios):
    print("Usuário não encontrado")