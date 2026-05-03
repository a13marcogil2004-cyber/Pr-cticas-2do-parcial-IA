from collections import deque

def bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]

    # Colas para ambos lados
    cola_inicio = deque([inicio])
    cola_objetivo = deque([objetivo])

    # Visitados y padres
    visitados_inicio = {inicio}
    visitados_objetivo = {objetivo}

    padres_inicio = {inicio: None}
    padres_objetivo = {objetivo: None}

    while cola_inicio and cola_objetivo:

        # Expandir desde inicio
        interseccion = expandir(
            grafo, cola_inicio, visitados_inicio, padres_inicio, visitados_objetivo
        )
        if interseccion:
            return construir_camino(interseccion, padres_inicio, padres_objetivo)

        # Expandir desde objetivo
        interseccion = expandir(
            grafo, cola_objetivo, visitados_objetivo, padres_objetivo, visitados_inicio
        )
        if interseccion:
            return construir_camino(interseccion, padres_inicio, padres_objetivo)

    return None


def expandir(grafo, cola, visitados, padres, visitados_opuesto):
    nodo = cola.popleft()

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            visitados.add(vecino)
            padres[vecino] = nodo
            cola.append(vecino)

            if vecino in visitados_opuesto:
                return vecino  # punto de encuentro

    return None


def construir_camino(nodo, padres_inicio, padres_objetivo):
    # Camino desde inicio
    camino_inicio = []
    actual = nodo
    while actual:
        camino_inicio.append(actual)
        actual = padres_inicio[actual]
    camino_inicio.reverse()

    # Camino desde objetivo
    camino_objetivo = []
    actual = padres_objetivo[nodo]
    while actual:
        camino_objetivo.append(actual)
        actual = padres_objetivo[actual]

    return camino_inicio + camino_objetivo


# Grafo ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Ejecutar
camino = bidireccional(grafo, 'A', 'F')

if camino:
    print("Camino encontrado:", " -> ".join(camino))
else:
    print("No se encontró camino")
