estados = ["Seguro", "Peligro"]

belief = {
    "Seguro": 0.6,
    "Peligro": 0.4
}

observacion = "Ruido"

modelo_observacion = {
    ("Ruido", "Seguro"): 0.2,
    ("Ruido", "Peligro"): 0.8
}

nuevo_belief = {}

total = 0

for estado in estados:

    prob = (
        belief[estado]
        * modelo_observacion[(observacion, estado)]
    )

    nuevo_belief[estado] = prob
    total += prob

for estado in estados:
    nuevo_belief[estado] /= total

print("Nuevo belief state:")
print(nuevo_belief)