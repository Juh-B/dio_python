menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

balance = 0
limit = 500
statement = ""
nbr_withdraw = 0
WITHDRAW_LIMITS = 3

while True:
	option = input(menu)

	if option == '1':
		value = float(input("Informe o valor do depósito: "))

		if value > 0:
			balance += value
			statement += f"Depósito: R$ {value:.2f}\n"
			print(f"\nDepósito de R${value:.2f} realizado com sucesso.")
		else:
			print("Erro! O Valor informado é inválido.")

	elif option == '2':
		value = float(input("Informe o valor do saque: "))

		exceeded_balance = value > balance
		exceeded_limit = value > limit
		exceeded_withdraws = nbr_withdraw >= WITHDRAW_LIMITS

		if exceeded_balance:
			print("Erro! Você não tem saldo suficiente.")

		elif exceeded_limit:
			print("Erro! O valor do saque excede o limite.")

		elif exceeded_withdraws:
			print("Erro! Número máximo de saques excedido.")

		elif value > 0:
			balance -= value
			statement += f"Saque: R$ {value:.2f}\n"
			nbr_withdraw += 1
			print(f"\nSaque de R${value:.2f} realizado com sucesso.")

		else:
			print("Erro! O Valor informado é inválido.")

	elif option == '3':
		print("\n---------- EXTRATO ----------")
		print("Não foram realizadas movimentações." if not statement else statement)
		print(f"\nSaldo: R$ {balance:.2f}")
		print("-----------------------------")

	elif option == '0':
		break

	else:
		print("Erro. Por favor selecione novamente o número da operação desejada.")
