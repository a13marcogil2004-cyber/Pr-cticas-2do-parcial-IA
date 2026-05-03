def dls(grafo, nodo, objetivo, limite, profundidad=0, visitados=None):
    if visitados is None:
        visitados = set()

    visitados.add(nodo)

    # Si encontramos el objetivo
    if nodo == objetivo:
        return [nodo]

    # Si llegamos al límite, detenemos
    if profundidad == limite:
        return None

    # Explorar vecinos
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            resultado = dls(grafo, vecino, objetivo, limite, profundidad + 1, visitados)

            if resultado is not None:
                return [nodo] + resultado

    return None


# Grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Parámetros
inicio = 'A'
objetivo = 'F'
limite = 2

camino = dls(grafo, inicio, objetivo, limite)

if camino:
    print("Camino encontrado:", " -> ".join(camino))
else:
    print("No se encontró dentro del límite")
