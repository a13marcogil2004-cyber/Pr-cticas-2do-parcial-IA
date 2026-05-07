estados = ["Inicio", "Meta"]

acciones = {
    "Inicio": ["Avanzar"],
    "Meta": []
}

transiciones = {
    ("Inicio", "Avanzar"): "Meta"
}

recompensas = {
    ("Inicio", "Avanzar"): 10
}

gamma = 0.9

valores = {
    estado: 0
    for estado in estados
}

for _ in range(10):

    nuevos = valores.copy()

    for estado in estados:

        if estado == "Meta":
            continue

        mejores = []

        for accion in acciones[estado]:

            siguiente = transiciones[(estado, accion)]

            valor = (
                recompensas[(estado, accion)]
                + gamma * valores[siguiente]
            )

            mejores.append(valor)

        nuevos[estado] = max(mejores)

    valores = nuevos

print(valores)