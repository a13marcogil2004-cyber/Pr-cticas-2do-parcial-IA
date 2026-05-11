estado = "casa"

objetivo = "universidad"

acciones = {
    "casa": "autobus",
    "autobus": "universidad"
}

camino = []

while estado != objetivo:

    camino.append(estado)

    estado = acciones[estado]

camino.append(objetivo)

print("Plan generado:\n")

for paso in camino:
    print("-", paso)