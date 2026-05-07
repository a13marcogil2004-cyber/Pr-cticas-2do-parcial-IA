variables = ["A", "B", "C"]

dominios = {
    "A": [1, 2],
    "B": [1, 2],
    "C": [1, 2]
}

restricciones = [
    ("A", "B"),
    ("B", "C")
]

def consistente(asignacion):

    for x, y in restricciones:

        if x in asignacion and y in asignacion:
            if asignacion[x] == asignacion[y]:
                return False

    return True

def resolver(arreglo, restantes):

    if not restantes:
        return arreglo

    variable = restantes[0]

    for valor in dominios[variable]:

        arreglo[variable] = valor

        if consistente(arreglo):

            resultado = resolver(
                arreglo,
                restantes[1:]
            )

            if resultado:
                return resultado

        del arreglo[variable]

    return None

cutset = ["B"]

for valor in dominios["B"]:

    asignacion = {"B": valor}

    resultado = resolver(
        asignacion,
        ["A", "C"]
    )

    if resultado:
        print("Solución:", resultado)
        break