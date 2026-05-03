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
    # (costo, nodo, camino)
    cola = [(0, inicio, [])]
    visitados = set()

