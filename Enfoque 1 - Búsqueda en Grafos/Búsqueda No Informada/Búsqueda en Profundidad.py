def dfs_iterativo(grafo, inicio):
    visitados = set()
    pila = [inicio]
    recorrido = []

    while pila:
        nodo = pila.pop()

        if nodo not in visitados:
            visitados.add(nodo)
            recorrido.append(nodo)

            # Se invierte para mantener orden lógico
            for vecino in reversed(grafo[nodo]):
                if vecino not in visitados:
                    pila.append(vecino)

    return recorrido


# Grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

resultado = dfs_iterativo(grafo, 'A')
print("Recorrido DFS:", resultado)
