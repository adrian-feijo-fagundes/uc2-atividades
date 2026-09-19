valor_compra = float(input("Qual o valor da compra? ")) 

desconto = 0

if valor_compra >= 500:
    desconto = 15
elif valor_compra >= 300:
    desconto = 10
elif valor_compra >= 100:
    desconto = 5

valor_desconto = valor_compra * (desconto / 100)
valor_final = valor_compra - valor_desconto

print(f"\nValor da compra: {valor_compra}\n")
print(f"Valor original: R$ {valor_compra}")
print(f"Desconto: {desconto}%")
print(f"Valor do desconto: R$ {valor_desconto}")
print(f"Valor final: R$ {valor_final}")


