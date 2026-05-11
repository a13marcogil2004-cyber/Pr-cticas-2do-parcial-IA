mediciones = [
    10,
    12,
    11,
    13,
    12
]

estimacion = 10

for medicion in mediciones:

    prediccion = estimacion

    ganancia = 0.5

    estimacion = (
        prediccion
        +
        ganancia
        *
        (medicion - prediccion)
    )

    print(
        "Estimación:",
        round(estimacion, 2)
    )