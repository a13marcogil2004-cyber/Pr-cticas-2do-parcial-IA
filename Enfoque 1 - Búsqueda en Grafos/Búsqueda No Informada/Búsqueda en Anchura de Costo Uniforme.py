import heapq  # cola de prioridad

# Grafo con costos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

def ucs(grafo, inicio, objetivo):
    cola = [(0, inicio, [])]  # (costo, nodo, camino)
    visitados = set()

    while cola:
        costo, nodo, camino = heapq.heappop(cola)

        if nodo in visitados:
            continue

        camino = camino + [nodo]
        visitados.add(nodo)

        if nodo == objetivo:
            return costo, camino

        for vecino, peso in grafo[nodo]:
            if vecino not in visitados:
                heapq.heappush(cola, (costo + peso, vecino, camino))

    return None


# Ejecutar
resultado = ucs(grafo, 'A', 'F')

if resultado:
    costo, camino = resultado
    print("Costo mínimo:", costo)
    print("Camino:", " -> ".join(camino))
else:
    print("No se encontró camino")