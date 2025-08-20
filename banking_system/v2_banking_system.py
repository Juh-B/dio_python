import textwrap

def menu():
	menu = """\n
	-------- MENU --------
	[1]\tDepositar
	[2]\tSacar
	[3]\tExtrato

 	[4]\tNovo usuário
	[5]\tListar usuários

	[6]\tNova conta
	[7]\tListar contas

	[0]\tSair

	"""
	return input(textwrap.dedent(menu))


def make_deposit(balance, value, statement, /):
	if value > 0:
		balance += value
		statement += f"Depósito:\tR$ {value:.2f}\n"
		print(f"\n-- Depósito de R${value:.2f} realizado com sucesso. --")
	else:
		print("Erro! O Valor informado é inválido.")

	return balance, statement


def make_withdraw(*, balance, value, statement, limit, nbr_withdraw, withdraw_limit):
	exceeded_balance = value > balance
	exceeded_limit = value > limit
	exceeded_withdraws = nbr_withdraw >= withdraw_limit

	if exceeded_balance:
		print("Erro! Você não tem saldo suficiente.")

	elif exceeded_limit:
		print("Erro! O valor do saque excede o limite.")

	elif exceeded_withdraws:
		print("Erro! Número máximo de saques excedido.")

	elif value > 0:
		balance -= value
		statement += f"Saque:\t\tR$ {value:.2f}\n"
		nbr_withdraw += 1
		print(f"\n-- Saque de R${value:.2f} realizado com sucesso. --")

	else:
		print("Erro! O Valor informado é inválido.")

	return balance, statement, nbr_withdraw


def show_statement(balance, /, *, statement):
	print("\n---------- EXTRATO ----------")
	print("Não foram realizadas movimentações." if not statement else statement)
	print(f"\nSaldo:\t\tR$ {balance:.2f}")
	print("-----------------------------")


def find_user(cpf, users):
	used_cpf = [user for user in users if user["cpf"] == cpf]
	return used_cpf[0] if used_cpf else None


def new_user(users):
	cpf = input("Informe o CPF (somente números): ")
	user = find_user(cpf, users)

	if user:
		print("Erro. Já existe usuário com esse CPF!")
		return

	name = input("Informe o nome Completo: ")
	birthday = input("Informe a data de nascimento (dd-mm-aaaa): ")
	address = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

	users.append({"name": name, "birthday": birthday, "cpf": cpf, "address": address})
	print("\n-- Usuário criado com sucesso! --")


def show_users(users):
	for user in users:
		line = f"""\
			Titular:\t{user['name']}
			CPF:\t\t{user['cpf']}
		"""
		print("-" * 40)
		print(textwrap.dedent(line))


def new_account(ag, nbr_account, users):
	cpf = input("Informe o CPF do usuário: ")
	user = find_user(cpf, users)

	if user:
		print("\n-- Conta criada com sucesso --")
		return {"Ag": ag, "nbr_account": nbr_account, "user": user}

	print("\nErro. Usuário não encontrado.\nFluxo de criação de conta encerrado!")


def show_accounts(accounts):
	for account in accounts:
		line = f"""\
			Ag:\t\t{account['Ag']}
			CC:\t\t{account['nbr_account']}
			Titular:\t{account['user']['name']}
		"""
		print("=" * 35)
		print(textwrap.dedent(line))


def main():
	WITHDRAW_LIMITS = 3
	AG = "0001"

	balance = 0
	limit = 500
	statement = ""
	nbr_withdraw = 0
	users = []
	accounts = []
	nbr_account = 1

	while True:
		option = menu()

		if option == '1':
			value = float(input("Informe o valor do depósito: "))

			balance, statement = make_deposit(balance, value, statement)

		elif option == '2':
			value = float(input("Informe o valor do saque: "))

			balance, statement, nbr_withdraw = make_withdraw(
				balance=balance,
				value=value,
				statement=statement,
				limit=limit,
				nbr_withdraw=nbr_withdraw,
				withdraw_limit=WITHDRAW_LIMITS,
			)

		elif option == '3':
			show_statement(balance, statement=statement)

		elif option == '4':
			new_user(users)

		elif option == '5':
			show_users(users)

		elif option == '6':
			account = new_account(AG, nbr_account, users)

			if account:
				accounts.append(account)
				nbr_account += 1

		elif option == '7':
			show_accounts(accounts)

		elif option == '0':
			break

		else:
			print("Erro. Por favor selecione novamente o número da operação desejada.")

main()
