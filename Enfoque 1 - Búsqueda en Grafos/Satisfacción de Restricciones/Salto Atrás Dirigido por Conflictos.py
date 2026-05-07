def es_valido(asignacion, variable, valor, restricciones):

    for var2 in asignacion:

        if (variable, var2) in restricciones:
            if asignacion[var2] == valor:
                return False, var2

        if (var2, variable) in restricciones:
            if asignacion[var2] == valor:
                return False, var2

    return True, None

def backjumping(variables, dominios, restricciones, asignacion={}):

    if len(asignacion) == len(variables):
        return asignacion

    variable = [v for v in variables if v not in asignacion][0]

    conflictos = set()

    for valor in dominios[variable]:

        valido, conflicto = es_valido(asignacion, variable, valor, restricciones)

        if valido:

            asignacion[variable] = valor

            resultado = backjumping(
                variables,
                dominios,
                restricciones,
                asignacion
            )

            if resultado:
                return resultado

            del asignacion[variable]

        else:
            conflictos.add(conflicto)

    return None

variables = ["A", "B", "C"]

dominios = {
    "A": [1,2,3],
    "B": [1,2,3],
    "C": [1,2,3]
}

restricciones = {
    ("A","B"),
    ("B","C")
}

solucion = backjumping(
    variables,
    dominios,
    restricciones
)

print(solucion)