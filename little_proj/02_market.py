# Descrição
# Crie um sistema de carrinho de compras que permita adicionar produtos
# e calcular o valor total da compra.

# Entrada
# Lista de produtos adicionados ao carrinho (cada um com nome e preço).

# Saída
# Lista dos produtos adicionados e o total da compra.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas
# respectivas saídas esperadas. Certifique-se de testar seu programa com esses
# exemplos e com outros casos possíveis.

# Entrada			Saída
# 2					Pão: R$3.50
# Pão 3.50			Leite: R$4.00
# Leite 4.00		Total: R$7.50
#
# 3					Arroz: R$2.50
# Arroz 2.50		Brigadeiro: R$3.00
# Brigadeiro 3.00	Sorvete: R$14.50
# Sorvete 14.50		Total: R$20.00
#
# 3					Maçã: R$2.00
# Maçã 2.00			Pera: R$3.50
# Pera 3.50			Biscoito: R$5.50
# Biscoito 5.50		Total: R$11.00

# ------------------------------------------------------------------------------

# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input("Quantos itens deseja adicionar?\n").strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input("Adicione novos produtos ('Produto valor')\n").strip()

    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")

    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])

    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# Exiba os itens e o total da compra
for item in carrinho:
	print(f"{item[0]}: R${item[1]:.2f}")
print(f"Total: R${total:.2f}")
