import random

# Pedra   = 0
# Papel   = 1
# Tesoura = 2
print("""
    0.Pedra   
    1.Papel   
    2.Tesoura
    """)
player = int(input("Digite o número de sua escolha: "))
ia = random.randint(0, 2)
jogadas = ["Pedra","Papel","Tesoura"]

print(f"Você jogou {jogadas[player]} e a máquina {jogadas[ia]}")

if player == ia:
    print("Empate")
else:   
    if (player == 0 and ia == 2): 
        print("Jogador venceu")
    elif (player == 2 and ia == 0):
        print("Máquina venceu")
    else:
        if player > ia:
            print("Jogador venceu")
        else:    
            print("Máquina venceu")

