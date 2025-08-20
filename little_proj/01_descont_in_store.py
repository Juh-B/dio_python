# Dicionário com os valores de desconto
descontos = {
	"DESCONTO10": 0.10,
	"DESCONTO20": 0.20,
	"SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input("Preço do produto: ").strip())
cupom = input("Código do cupom: ").strip()

# Aplicando o desconto se o cupom for válido:
if preco > 0:
	if cupom in descontos:
		valor_desconto = descontos[cupom]
		preco_final = preco * (1 - valor_desconto)
		print(f"Preço com desconto: {preco_final:.2f}")
	else:
		print("Cupom inválido.")
else:
	print("Valor do produto inválido.")
