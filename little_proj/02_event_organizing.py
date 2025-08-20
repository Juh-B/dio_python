# Descrição
# Uma empresa quer criar um organizador de eventos que divida os participantes
# em grupos de acordo com o tema escolhido.

# Entrada
# Lista de participantes e o tema escolhido por cada um.

# Saída
# Dicionário agrupando os participantes por tema.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas
# respectivas saídas esperadas. Certifique-se de testar seu programa com esses
# exemplos e com outros casos possíveis.

# Entrada					Saída
# 3							Fotografia: Lucas, Carlos
# Lucas, Fotografia			Viagem: Ana
# Ana, Viagem
# Carlos, Fotografia

# 4							Música: João, Pedro
# João, Música				Dança: Maria, Ana
# Pedro, Música
# Maria, Dança
# Ana, Dança

# 5							Tecnologia: Ana, Maria
# Ana, Tecnologia			Esportes: Carlos, João
# Carlos, Esportes			Música: Pedro
# Maria, Tecnologia
# Pedro, Música
# João, Esportes

# ------------------------------------------------------------------------------

# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input("Numero de participantes: ").strip())

# Loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input("Adicione participante ('Nome, Tema')\n").strip()

    # Divide a linha em duas partes: nome e tema
    nome, tema = linha.split(",")

    # Remove espaços extras
    nome = nome.strip()
    tema = tema.strip()

    # Adiciona ao dicionário
    if tema not in eventos:
        eventos[tema] = []  # cria a lista se o tema não existir ainda
    eventos[tema].append(nome)


# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
