"""
Você tera que criar uma classe carro que vai possuir dois atributos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método aceletar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:

1) Valor de direção com valores possívies: Norte, Sul, Leste, Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda


  N
O   L
  S

    Exemplo:
    >>> # Teste Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3

    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> # Teste Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'NORTE'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'LESTE'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'SUL'

    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'OESTE'


    >>> direcao.valor
    'OESTE'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'SUL'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'LESTE'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'NORTE'
"""

class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def verificar_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        return self.motor.girar_a_direita()

    def girar_a_esquerda(self):
        return self.motor.girar_a_esquerda()


class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


class Direcao:

    def __init__(self):
        self.valor = 'NORTE'

    direcoes_a_direita = {
        'NORTE': 'LESTE',
        'LESTE': 'SUL',
        'SUL': 'OESTE',
        'OESTE': 'NORTE'
    }

    direcoes_a_esquerda = {
        'NORTE': 'OESTE',
        'OESTE': 'SUL',
        'SUL': 'LESTE',
        'LESTE': 'NORTE'
    }

    def girar_a_direita(self):
        self.valor = self.direcoes_a_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.direcoes_a_esquerda[self.valor]



if __name__ == '__main__':
    motor = Motor
    direcao = Direcao
    carro = Carro(motor, direcao)



    carro.calcular_velocidade()
    # 0
    carro.motor.acelerar()
    carro.calcular_velocidade()
    # 1
    carro.motor.acelerar()
    carro.calcular_velocidade()
    # 2
    carro.motor.acelerar()
    carro.calcular_velocidade()
    # 3


    carro.motor.frear()
    carro.calcular_velocidade()
    # 1
    carro.motor.frear()
    carro.calcular_velocidade()
    # 0


    carro.verificar_direcao()
    # Norte
    carro.direcao.girar_a_direita()
    carro.verificar_direcao()
    # Leste
    carro.direcao.girar_a_direita()
    carro.verificar_direcao()
    # Sul

    carro.direcao.girar_a_direita()
    carro.verificar_direcao()
    # Oeste


    carro.verificar_direcao()
    # Oeste
    carro.direcao.girar_a_esquerda()
    carro.verificar_direcao()
    # Sul
    carro.direcao.girar_a_esquerda()
    carro.verificar_direcao()
    # Leste
    carro.direcao.girar_a_esquerda()
    carro.verificar_direcao()
    # Norte