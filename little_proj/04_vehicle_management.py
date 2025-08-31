# Descrição
# Implemente uma classe Veiculo que represente um carro com marca, modelo e ano.
# Crie um método que verifique se o carro é considerado antigo (mais de 20 anos).

# Entrada
# Marca, modelo e ano do veículo.

# Saída
# "Veículo antigo" se o carro tiver mais de 20 anos.
# "Veículo novo" caso contrário.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e
# suas respectivas saídas esperadas. Certifique-se de testar seu programa
# com esses exemplos e com outros casos possíveis.

# Entrada		Saída
# Toyota		Veículo antigo
# Corolla
# 2000

# Honda		Veículo novo
# Civic
# 2005

# Ford		Veículo antigo
# Fiesta
# 1999

# ------------------------------------------------------------------------------

from datetime import datetime

# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:
# TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:

class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def verificar_antiguidade(self):
        antiguidade = datetime.now().year - self.ano
        return "Veículo antigo" if antiguidade > 20 else "Veículo novo"

# Entrada direta
marca = input("Marca do veiculo: ").strip()
modelo = input("Modelo: ").strip()
ano = int(input("Ano: ").strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())
