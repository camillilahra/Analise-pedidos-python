import csv

def limpar_pedido(linha):
    try:
        quantidade = int(linha["quantidade"])
        preco = float(linha["preco_unitario"])
    except:
        return None

    if quantidade <= 0:
        return None

    if preco <= 0:
        return None

    linha["quantidade"] = quantidade
    linha["preco_unitario"] = preco
    return linha

arquivo = open("pedidos.csv", encoding="utf-8")
leitor = csv.DictReader(arquivo)

pedidos = []

for linha in leitor:
    pedido_limpo = limpar_pedido(linha)
    if pedido_limpo is not None:
        pedidos.append(pedido_limpo)

print("Total de pedidos válidos:", len(pedidos))

quantidades = []

for pedido in pedidos:
    quantidades.append(pedido["quantidade"])

media_quantidade = sum(quantidades) / len(quantidades)
limite_suspeito = media_quantidade * 5

print("Média de quantidade por pedido:", round(media_quantidade, 2))

pedidos_normais = []
pedidos_suspeitos = []

for pedido in pedidos:
    if pedido["quantidade"] > limite_suspeito:
        pedidos_suspeitos.append(pedido)
    else:
        pedidos_normais.append(pedido)

gastos_por_cliente = {}

for pedido in pedidos_normais:
    cliente = pedido["cliente"]
    valor = pedido["quantidade"] * pedido["preco_unitario"]

    if cliente not in gastos_por_cliente:
        gastos_por_cliente[cliente] = 0

    gastos_por_cliente[cliente] = gastos_por_cliente[cliente] + valor

print("\nTotal gasto por cliente:")
for cliente, total in gastos_por_cliente.items():
    print(cliente, "-> R$", round(total, 2))

quantidade_por_produto = {}
faturamento_total = 0

for pedido in pedidos_normais:
    produto = pedido["produto"]
    quantidade = pedido["quantidade"]
    valor = pedido["quantidade"] * pedido["preco_unitario"]

    if produto not in quantidade_por_produto:
        quantidade_por_produto[produto] = 0

    quantidade_por_produto[produto] = quantidade_por_produto[produto] + quantidade
    faturamento_total = faturamento_total + valor

produto_mais_vendido = max(quantidade_por_produto, key=quantidade_por_produto.get)

print("\nProduto mais vendido:", produto_mais_vendido, "-", quantidade_por_produto[produto_mais_vendido], "unidades")
print("Faturamento total: R$", round(faturamento_total, 2))

print("\nPedidos suspeitos (quantidade muito acima da média, excluídos dos cálculos acima):")
for pedido in pedidos_suspeitos:
    print("-", pedido["id_pedido"], pedido["cliente"], pedido["produto"], "- quantidade:", pedido["quantidade"])

arquivo.close()