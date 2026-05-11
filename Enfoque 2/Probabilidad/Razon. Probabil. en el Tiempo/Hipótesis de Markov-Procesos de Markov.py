import random

estado = "Soleado"

for _ in range(10):

    print("Estado actual:", estado)

    numero = random.random()

    if estado == "Soleado":

        if numero < 0.7:
            estado = "Soleado"

        else:
            estado = "Lluvioso"

    else:

        if numero < 0.6:
            estado = "Lluvioso"

        else:
            estado = "Soleado"