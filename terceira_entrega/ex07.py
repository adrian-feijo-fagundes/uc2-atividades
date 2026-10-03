frase = input("Digite uma frase: ").lower()

qtd_letra_a = 0

for letra in frase:
    if letra == "a":
        qtd_letra_a += 1


print(f"A frase tem {qtd_letra_a} letras \"a\"")