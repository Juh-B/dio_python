# print("Hello W")
# print(True)
# print(False)
# print(4 * 5)

# modo interativo -> python3 -i ./prog_name
# para sair do modo interativo -> ctrl + D ou exit()

# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input("Preco do produto: ").strip())
cupom = input("Codigo do cupom: ").strip()

# Aplicando o desconto se o cupom for válido:
def aplicando_cupom(cupom):
  if cupom == "DESCONTO10"
