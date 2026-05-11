datos = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1)
]

pesos = [0.0, 0.0]

bias = 0.0

learning_rate = 0.1

def activacion(x):

    if x >= 0:
        return 1

    return 0

for _ in range(20):

    for entradas, salida_real in datos:

        suma = (
            entradas[0] * pesos[0]
            +
            entradas[1] * pesos[1]
            +
            bias
        )

        salida = activacion(suma)

        error = salida_real - salida

        pesos[0] += learning_rate * error * entradas[0]
        pesos[1] += learning_rate * error * entradas[1]

        bias += learning_rate * error

print("Pesos finales:")
print(pesos)

print("Bias:")
print(bias)

print("\nPredicciones:")

for entradas, _ in datos:

    suma = (
        entradas[0] * pesos[0]
        +
        entradas[1] * pesos[1]
        +
        bias
    )

    salida = activacion(suma)

    print(entradas, "->", salida)