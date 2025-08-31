import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def make_operation(self, accounts, operation):
        operation.register(accounts)

    def add_account(self, accounts):
        self.accounts.append(accounts)

class PersonalAccount(Client):
    def __init__(self, name, birthday, cpf, address):
        super().__init__(address)
        self.name = name
        self.birthday = birthday
        self.cpf = cpf

    def __str__(self):
        return f"""\
            Titular:\t{self.name}
            CPF:\t\t{self.cpf}
        """

class Account:
    def __init__(self, ac_number, client):
        self._balance = 0
        self._ac_number = ac_number
        self._branch = "0001"
        self._client = client
        self._historic = Historic()

    @classmethod
    def new_account(cls, client, ac_number):
        return cls(ac_number, client)

    @property
    def balance(self):
        return self._balance

    @property
    def ac_number(self):
        return self._ac_number

    @property
    def agency(self):
        return self._branch

    @property
    def client(self):
        return self._client

    @property
    def historic(self):
        return self._historic

    def make_withdraw(self, value):
        balance = self.balance
        exceeded_balance = value > balance

        if exceeded_balance:
            print("Erro! Você não tem saldo suficiente.")

        elif value > 0:
            self._balance -= value
            print(f"\n-- Saque de R${value:.2f} realizado com sucesso. --")
            return True

        else:
            print("Erro! O Valor informado é inválido.")

        return False

    def make_deposit(self, value):
        if value > 0:
            self._balance += value
            print(f"\n-- Depósito de R${value:.2f} realizado com sucesso. --")
        else:
            print("Erro! O Valor informado é inválido.")
            return False

        return True

class CurrentAccount(Account):
    def __init__(self, ac_number, client, limit=500, withdraw_limit=3):
        super().__init__(ac_number, client)
        self.limit = limit
        self.withdraw_limit = withdraw_limit

    def make_withdraw(self, value):
        nbr_withdraw = len(
            [operation for operation in self.historic.operations
            if operation["type"] == "Withdraw"]
        )

        exceeded_limit = value > self.limit
        exceeded_withdraws = nbr_withdraw >= self.withdraw_limit

        if exceeded_limit:
            print("Erro! O valor do saque excede o limite.")

        elif exceeded_withdraws:
            print("Erro! Número máximo de saques excedido.")

        else:
            return super().make_withdraw(value)

        return False

    def __str__(self):
        return f"""\
            Ag:\t\t{self._branch}
            Cc:\t\t{self.ac_number}
            Titular:\t{self.client.name}
        """

class Historic:
    def __init__(self):
        self._operations = []

    @property
    def operations(self):
        return self._operations

    def add_operation(self, operation):
        self._operations.append(
            {
                "type": operation.__class__.__name__,
                "value": operation.value,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

class Operation(ABC):
    @property
    @abstractproperty
    def value(self):
        pass

    @abstractclassmethod
    def register(self, account):
        pass

class Withdraw(Operation):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        successed_operation = account.make_withdraw(self.value)

        if successed_operation:
            account.historic.add_operation(self)

class Deposite(Operation):
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def register(self, account):
        successed_operation = account.make_deposit(self.value)

        if successed_operation:
            account.historic.add_operation(self)


# -----------------------------

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


def make_deposit(clients):
    cpf = input("Informe o CPF do cliente: ")
    client = find_client(cpf, clients)

    if not client:
        print("\nErro. Cliente não encontrado!")
        return

    value = float(input("Informe o valor do depósito: "))
    operation = Deposite(value)

    account = client_account(client)
    if not account:
        return

    client.make_operation(account, operation)


def make_withdraw(clients):
    cpf = input("Informe o CPF do cliente: ")
    client = find_client(cpf, clients)

    if not client:
        print("\nErro. Cliente não encontrado!")
        return

    value = float(input("Informe o valor do saque: "))
    operation = Withdraw(value)

    account = client_account(client)
    if not account:
        return

    client.make_operation(account, operation)


def show_statement(clients):
    cpf = input("Informe o CPF do cliente: ")
    client = find_client(cpf, clients)

    if not client:
        print("\nErro. Cliente não encontrado!")
        return

    account = client_account(client)
    if not account:
        return

    print("\n---------- EXTRATO ----------")
    operations = account.historic.operations

    statement = ""
    if not operations:
        statement = "Não foram realizadas movimentações."
    else:
        for operation in operations:
            operation_type = "[+]" if operation['type'] == "Deposite" else "[-]"
            statement += f"\n{operation_type}\t\tR$ {operation['value']:.2f}"

    print(statement)
    print(f"\nSaldo:\t\tR$ {account.balance:.2f}")
    print("-----------------------------")


def find_client(cpf, clients):
    filter_clients = [client for client in clients if client.cpf == cpf]
    return filter_clients[0] if filter_clients else None


def client_account(client):
    if not client.accounts:
        print("Erro! Cliente ainda não possui conta!")
        return

    return client.accounts[0]


def new_client(clients):
    cpf = input("Informe o CPF (somente números): ")
    client = find_client(cpf, clients)

    if client:
        print("Erro. Já existe usuário com esse CPF!")
        return

    name = input("Informe o nome Completo: ")
    birthday = input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    client = PersonalAccount(name=name, birthday=birthday, cpf=cpf, address=address)
    clients.append(client)

    print("\n-- Cliente criado com sucesso! --")


def show_clients(clients):
    for client in clients:
        print("-" * 40)
        print(textwrap.dedent(str(client)))


def new_account(nbr_account, clients, accounts):
    cpf = input("Informe o CPF do cliente: ")
    client = find_client(cpf, clients)

    if not client:
        print("\nErro. Usuário não encontrado.\nFluxo de criação de conta encerrado!")
        return

    n_account = CurrentAccount.new_account(client=client, ac_number=nbr_account)
    accounts.append(n_account)
    client.accounts.append(n_account)
    print("\n-- Conta criada com sucesso --")


def show_accounts(accounts):
    for account in accounts:
        print("=" * 35)
        print(textwrap.dedent(str(account)))


def main():
    clients = []
    accounts = []

    while True:
        option = menu()

        if option == '1':
            make_deposit(clients)

        elif option == '2':
            make_withdraw(clients)

        elif option == '3':
            show_statement(clients)

        elif option == '4':
            new_client(clients)

        elif option == '5':
            show_clients(clients)

        elif option == '6':
            nbr_account = len(accounts) + 1
            new_account(nbr_account, clients, accounts)

        elif option == '7':
            show_accounts(accounts)

        elif option == '0':
            break

        else:
            print("Erro. Por favor selecione novamente o número da operação desejada.")

main()
