
import random

num_lancamentos = 1000


def gera():
    return random.randint(1, 6)


def lancamento(num_lancamentos):

    for val in range(num_lancamentos):
        dado1 = gera()
        dado2 = gera()

        somatoria_dados = dado1 + dado2

        return somatoria_dados, dado1, dado2, val


resultado = lancamento(num_lancamentos)

print("Número aleatório gerado:", resultado)