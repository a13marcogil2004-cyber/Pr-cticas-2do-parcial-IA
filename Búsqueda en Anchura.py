from collections import deque

# Grafo representado como diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])

    while cola:
        nodo = cola.popleft()

        if nodo not in visitados:
            print(nodo, end=" ")
            visitados.add(nodo)

            # Agregar vecinos a la cola
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

# Ejecutar BFS desde el nodo A
bfs(grafo, 'A')