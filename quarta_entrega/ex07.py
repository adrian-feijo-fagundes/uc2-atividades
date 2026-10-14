produtos = []
precos = []


while True:
    produto = input("Nome do produto: ")
    preco = input("Preço: ")
    if produto.lower() == "sair" or preco.lower() == "sair":
        break 
    produtos.append(produto)
    precos.append(int(preco))

print(f"Quantidade de produtos cadastrados: {len(produtos)}")
print(f"Valor total da compra: {sum(precos)}")
contador = 0
maior_preco = max(precos)
menor_preco = min(precos)

while contador < len(produtos):
    if precos[contador] == menor_preco:
        print(f"Produto mais barato: {produtos[contador]} com valor de {menor_preco}")
    if precos[contador] == maior_preco:
        print(f"Produto mais caro: {produtos[contador]} com valor de {maior_preco}")
    contador += 1
