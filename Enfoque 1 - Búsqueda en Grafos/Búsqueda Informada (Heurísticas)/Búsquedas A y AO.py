# Código A*
import heapq

def heuristica(nodo):
    h = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 0
    }
    return h[nodo]


def a_estrella(grafo, inicio, objetivo):
    cola = [(0, inicio, [])]
    visitados = set()

    while cola:
        f, nodo, camino = heapq.heappop(cola)

        if nodo in visitados:
            continue

        camino = camino + [nodo]
        visitados.add(nodo)

        if nodo == objetivo:
            return camino

        for vecino, costo in grafo[nodo]:
            g = costo
            h = heuristica(vecino)
            heapq.heappush(cola, (g + h, vecino, camino))

    return None


# Grafo con costos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

print("A*:", " -> ".join(a_estrella(grafo, 'A', 'D')))