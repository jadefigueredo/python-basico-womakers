# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.


class Carro:
    def __init__(self, ligado, cor, modelo, velocidade):
        self.ligado = ligado
        self.cor = cor
        self.modelo = modelo
        self.velocidade = velocidade

# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
def liga(self):
    self.ligado = True

def desliga(self):
    self.ligado = False

def acelera(self, velocidade):
    if not self.ligado:
        print("O carro está desligado. Não é possível acelerar.")
        return
    self.velocidade += velocidade
    print(f"O carro acelerou para {self.velocidade} km/h.")

def desacelera(self, velocidade):
    if not self.ligado:
        print("O carro está desligado. Não é possível desacelerar.")
        return
    if self.velocidade < velocidade:
        self.velocidade = 0
        print(f"O carro não pode ser desacelerado pois já está parado.")
        return
    self.velocidade -= velocidade
    print(f"O carro desacelerou para {self.velocidade} km/h.")


# Crie uma instância da classe carro.
carro = Carro(True, 'Azul', 'Creta', 15)

# Faça o carro "andar" utilizando os métodos da sua classe.
carro.liga()
carro.acelera(5)

# Faça o carro "parar" utilizando os métodos da sua classe.

carro.desacelera(5)
carro.desliga()