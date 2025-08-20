# Entrada do usuário
email = input("Digite seu e-mail: ").strip()

# Verificação
if (
    "@" in email                                  # tem arroba
    and "." in email.split("@")[-1]               # tem ponto no domínio
    and not email.startswith("@")                 # não começa com @
    and not email.endswith("@")                   # não termina com @
    and " " not in email                          # não tem espaços
):
    print("E-mail válido")
else:
    print("E-mail inválido")
