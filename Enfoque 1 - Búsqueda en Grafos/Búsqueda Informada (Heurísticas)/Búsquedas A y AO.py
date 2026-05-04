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

#--------------------------------------------------------------------------------------------------------------

# Código AO*

def ao_estrella(grafo, nodo, heuristica):
    # Si es nodo final
    if nodo not in grafo:
        return nodo

    print(f"Evaluando nodo: {nodo}")

    # Seleccionar la mejor opción
    mejor_costo = float('inf')
    mejor_camino = []

    for opcion in grafo[nodo]:
        costo_total = 0
        camino_actual = []

        for subnodo in opcion:
            costo_total += heuristica[subnodo]
            camino_actual.append(subnodo)

        if costo_total < mejor_costo:
            mejor_costo = costo_total
            mejor_camino = camino_actual

    resultado = []
    for n in mejor_camino:
        resultado.append(ao_estrella(grafo, n, heuristica))

    return [nodo] + resultado


# Grafo AND-OR
grafo = {
    'A': [['B'], ['C', 'D']],
    'B': [['E']],
    'C': [['F']],
    'D': [['G']]
}

heuristica = {
    'B': 2,
    'C': 3,
    'D': 1,
    'E': 0,
    'F': 0,
    'G': 0
}

print("AO*:", ao_estrella(grafo, 'A', heuristica))