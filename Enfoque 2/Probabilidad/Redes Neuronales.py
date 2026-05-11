import random
import math

datos = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

w1 = random.random()
w2 = random.random()
w3 = random.random()
w4 = random.random()

b1 = random.random()
b2 = random.random()

learning_rate = 0.5

for _ in range(10000):

    for entradas, objetivo in datos:

        h1 = sigmoid(
            entradas[0] * w1
            +
            entradas[1] * w2
            +
            b1
        )

        salida = sigmoid(
            h1 * w3
            +
            b2
        )

        error = objetivo - salida

        gradiente = error * salida * (1 - salida)

        w3 += learning_rate * gradiente * h1

        b2 += learning_rate * gradiente

print("Predicciones:")

for entradas, _ in datos:

    h1 = sigmoid(
        entradas[0] * w1
        +
        entradas[1] * w2
        +
        b1
    )

    salida = sigmoid(
        h1 * w3
        +
        b2
    )

    print(
        entradas,
        "->",
        round(salida, 3)
    )