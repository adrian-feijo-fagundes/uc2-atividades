jogos = [
    "Minecraft",
    "Terraria",
    "Stardew Valley"
]

while len(jogos) < 5:
    jogos.append(input("Digite o nome de um jogo: "))

contador = 0
while contador < len(jogos):
    print(jogos[contador])
    contador += 1

print(f"\nQuantidade de jogos {len(jogos)}")
print(f"Primeiro jogo: {jogos[0]}")
print(f"Ultimo jogo: {jogos[len(jogos) - 1 ]}")