def heuristica(nodo):
    # Estimación de distancia al objetivo (menor = mejor)
    h = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 0
    }
    return h[nodo]


def busqueda_voraz(grafo, inicio, objetivo):
    actual = inicio
    camino = [actual]
    visitados = set()

    while actual != objetivo:
        visitados.add(actual)
        vecinos = grafo[actual]

        # Filtrar vecinos no visitados
        vecinos_no_visitados = [v for v in vecinos if v not in visitados]

        if not vecinos_no_visitados:
            return None  # No hay camino

        # Elegir el mejor según la heurística
        siguiente = min(vecinos_no_visitados, key=heuristica)

        camino.append(siguiente)
        actual = siguiente

    return camino


# Grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# Ejecutar
resultado = busqueda_voraz(grafo, 'A', 'D')

print("Camino encontrado:", " -> ".join(resultado))