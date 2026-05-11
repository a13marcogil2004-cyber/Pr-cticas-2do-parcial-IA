observaciones = [
    20,
    22,
    21,
    23,
    24
]

filtrado = (
    sum(observaciones)
    /
    len(observaciones)
)

prediccion = (
    filtrado
    +
    1
)

suavizado = (
    filtrado
    -
    0.5
)

print("Filtrado:")

print(round(filtrado, 2))

print("\nPredicción:")

print(round(prediccion, 2))

print("\nSuavizado:")

print(round(suavizado, 2))