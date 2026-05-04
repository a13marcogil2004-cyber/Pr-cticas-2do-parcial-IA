def heuristica(nodo):
    # Valor menor = mejor (más cerca del objetivo)
    h = {
        'A': 5,
        'B': 3,
        'C': 4,
        'D': 2,
        'E': 1,
        'F': 0
    }
    return h[nodo]


def ascension_colinas(grafo, inicio):
    actual = inicio
    camino = [actual]

    while True:
        vecinos = grafo[actual]

        # Si no hay vecinos, termina
        if not vecinos:
            break

        # Elegir el mejor vecino (menor heurística)
        mejor = min(vecinos, key=heuristica)

        # Si no mejora, se detiene (óptimo local)
        if heuristica(mejor) >= heuristica(actual):
            break

        actual = mejor
        camino.append(actual)

    return camino


# Grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Ejecutar
resultado = ascension_colinas(grafo, 'A')

print("Camino encontrado:", " -> ".join(resultado))