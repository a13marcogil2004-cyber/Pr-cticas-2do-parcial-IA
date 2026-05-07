estados = [0, 1, 2]

acciones = {
    0: [1],
    1: [2],
    2: [2]
}

recompensas = {
    0: 0,
    1: 1,
    2: 10
}

gamma = 0.9

politica = {
    0: 1,
    1: 2,
    2: 2
}

valores = {
    estado: 0
    for estado in estados
}

estable = False

while not estable:

    for _ in range(20):

        nuevos = valores.copy()

        for estado in estados:

            accion = politica[estado]

            nuevos[estado] = (
                recompensas[accion]
                + gamma * valores[accion]
            )

        valores = nuevos

    estable = True

    for estado in estados:

        accion_actual = politica[estado]

        mejor_accion = accion_actual
        mejor_valor = (
            recompensas[accion_actual]
            + gamma * valores[accion_actual]
        )

        for accion in acciones[estado]:

            valor = (
                recompensas[accion]
                + gamma * valores[accion]
            )

            if valor > mejor_valor:
                mejor_valor = valor
                mejor_accion = accion

        politica[estado] = mejor_accion

        if mejor_accion != accion_actual:
            estable = False

print("Política óptima:")
print(politica)

print("Valores:")
print(valores)