def dls(grafo, nodo, objetivo, limite, profundidad=0):
    # Caso base: encontramos el objetivo
    if nodo == objetivo:
        return [nodo]

    # Si llegamos al límite
    if profundidad == limite:
        return None

    # Explorar vecinos
    for vecino in grafo[nodo]:
        resultado = dls(grafo, vecino, objetivo, limite, profundidad + 1)

        if resultado is not None:
            return [nodo] + resultado

    return None


def ids(grafo, inicio, objetivo, max_profundidad):
    for limite in range(max_profundidad + 1):
        resultado = dls(grafo, inicio, objetivo, limite)

        if resultado is not None:
            return resultado, limite

    return None, None


# Grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Ejecutar
camino, nivel = ids(grafo, 'A', 'F', 5)

if camino:
    print("Camino encontrado:", " -> ".join(camino))
    print("Nivel encontrado:", nivel)
else:
    print("No se encontró solución")
