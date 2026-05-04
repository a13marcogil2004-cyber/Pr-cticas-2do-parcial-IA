import random

movimientos = [(-1,0),(1,0),(0,-1),(0,1)]

def es_valido(x, y, n, visitados):
    return 0 <= x < n and 0 <= y < n and (x,y) not in visitados

def online_search(n=5, objetivo=(4,4)):
    
    posicion = (0,0)
    visitados = set()
    visitados.add(posicion)

    camino = [posicion]

    while posicion != objetivo:
        
        vecinos = []

        for dx, dy in movimientos:
            nx, ny = posicion[0] + dx, posicion[1] + dy
            if es_valido(nx, ny, n, visitados):
                vecinos.append((nx, ny))

        if not vecinos:
            break

        siguiente = random.choice(vecinos)

        posicion = siguiente
        visitados.add(posicion)
        camino.append(posicion)

    return camino

camino = online_search()

print("Camino recorrido:")
print(camino)