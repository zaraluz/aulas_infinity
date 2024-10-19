produtos = []

while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))
    produtos.append({"nome": nome, "preco": preco})
    continuar = input("Deseja adicionar mais produtos? (s/n): ").lower()
    if continuar == 'n':
        break

total_gasto = sum(produto["preco"] for produto in produtos)

produto_mais_barato = min(produtos, key=lambda produto: produto["preco"])

produtos_acima_1000 = sum(1 for produto in produtos if produto["preco"] > 1000)

print(f"\nResumo da compra:")
print(f"Total gasto: R$ {total_gasto:.2f}")
print(f"Quantidade de produtos acima de R$1000: {produtos_acima_1000}")
print(f"Produto mais barato: {produto_mais_barato['nome']} (R$ {produto_mais_barato['preco']:.2f})")


