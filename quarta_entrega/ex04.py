produtos = []


while True:
    produto = input("Digite um produto: ")
    if produto.lower() == "fim":
        break
    produtos.append(produto)

contador = 0
while contador < len(produtos):
    print(produtos[contador])
    contador += 1

print(f"A quantidade de produtos cadastrados é {len(produtos)}")