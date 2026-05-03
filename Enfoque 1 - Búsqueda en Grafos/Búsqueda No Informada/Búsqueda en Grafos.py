from collections import deque

def busqueda_en_grafos(grafo, inicio, objetivo):
    cola = deque([inicio])
    visitados = set()
    padres = {inicio: None}

    while cola:
        nodo = cola.popleft()

        if nodo == objetivo:
            return reconstruir_camino(padres, inicio, objetivo)

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in grafo[nodo]:
                if vecino not in visitados and vecino not in cola:
                    padres[vecino] = nodo
                    cola.append(vecino)

    return None


def reconstruir_camino(padres, inicio, objetivo):
    camino = []
    actual = objetivo

    while actual is not None:
        camino.append(actual)
        actual = padres[actual]

    camino.reverse()
    return camino


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
camino = busqueda_en_grafos(grafo, 'A', 'F')

if camino:
    print("Camino encontrado:", " -> ".join(camino))
else:
    print("No se encontró camino")
