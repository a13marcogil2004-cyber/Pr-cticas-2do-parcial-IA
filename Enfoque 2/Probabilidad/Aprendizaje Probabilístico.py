datos = [
    ("Lluvioso", "Sí"),
    ("Soleado", "No"),
    ("Lluvioso", "Sí"),
    ("Nublado", "Sí"),
    ("Soleado", "No")
]

conteo = {}

for clima, jugar in datos:

    if clima not in conteo:
        conteo[clima] = {
            "Sí": 0,
            "No": 0
        }

    conteo[clima][jugar] += 1

def predecir(clima):

    if clima not in conteo:
        return "Desconocido"

    si = conteo[clima]["Sí"]
    no = conteo[clima]["No"]

    if si > no:
        return "Sí"
    else:
        return "No"

resultado = predecir("Lluvioso")

print("¿Jugar?")
print(resultado)