def heuristica(nodo):
    # Valores estimados al objetivo (mientras más bajo, más cerca)
    h = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 0
    }
    return h[nodo]


def busqueda_heuristica(grafo, inicio, objetivo):
    actual = inicio
    camino = [actual]

    while actual != objetivo:
        vecinos = grafo[actual]

        # Elegir el vecino con menor heurística
        siguiente = min(vecinos, key=heuristica)

        camino.append(siguiente)
        actual = siguiente

    return camino


# Grafo simple
grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# Ejecutar
resultado = busqueda_heuristica(grafo, 'A', 'D')

print("Camino encontrado:", " -> ".join(resultado))
