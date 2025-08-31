# Descrição
# Uma clínica médica quer automatizar seu sistema de atendimento.
# Crie uma função que organize os pacientes em ordem de prioridade
# com base na idade e na urgência do caso.

# 📌 Critérios de Prioridade:
# Pacientes acima de 60 anos têm prioridade.
# Pacientes que apresentam a palavra "urgente" na ficha têm prioridade máxima.
# Os demais pacientes são atendidos por ordem de chegada.

# Entrada
# Um número inteiro n, representando a quantidade de pacientes.
# n linhas seguintes, cada uma contendo os dados de um paciente
# no formato: nome, idade, status
# nome: string representando o nome do paciente.
# idade: número inteiro representando a idade do paciente.
# status: string que pode ser "urgente" ou "normal".

# Saída
# A saída deve exibir a lista dos pacientes ordenada de acordo com
# as regras de prioridade, no formato: Ordem de Atendimento: nome1, nome2, nome3, ...

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas
# respectivas saídas esperadas.
# Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada - 1
# 3
# Carlos, 40, normal
# Ana, 70, normal
# Bruno, 30, urgente

# Saída
# Ordem de Atendimento: Bruno, Ana, Carlos

# Entrada - 2
# 4
# Paula, 30, normal
# Ricardo, 60, normal
# Tiago, 60, urgente
# Amanda, 50, urgente

# Saída
# Ordem de Atendimento: Tiago, Amanda, Ricardo, Paula

# Entrada - 3
# 5
# João, 65, normal
# Maria, 80, urgente
# Lucas, 50, normal
# Fernanda, 25, normal
# Pedro, 90, urgente

# Saída
# Ordem de Atendimento: Pedro, Maria, João, Lucas, Fernanda

# ------------------------------------------------------------------------------

# Entrada do número de pacientes
n = int(input("Número de pacientes: ").strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input("Paciente por ordem de chegada (nome, idade, status):\n").strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# Ordene por prioridade: urgente > idosos > demais:
# Exiba a ordem de atendimento com título e vírgulas:

def prioridade(paciente):
    nome, idade, status = paciente
    if status.lower() == "urgente":
        return (0, -idade)  # prioridade 0 e ordena por idade desc
    elif idade >= 60:
        return (1, -idade)  # prioridade 1 e ordena por idade desc
    else:
        return (2, 0)  # prioridade 2, mantém ordem de chegada

# Ordena respeitando as regras
ordenados = sorted(pacientes, key=prioridade)

# Extrai só os nomes na ordem de atendimento
ordem = [nome for nome, _, _ in ordenados]

# Exibe resultado
print("Ordem de Atendimento: " + ", ".join(ordem))
