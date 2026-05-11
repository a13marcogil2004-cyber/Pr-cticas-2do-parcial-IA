frases = [
    "Juan estudia",
    "Ana trabaja",
    "Carlos estudia"
]

def analizar(frase):

    palabras = frase.split()

    sujeto = palabras[0]

    accion = palabras[1]

    return sujeto, accion

for frase in frases:

    sujeto, accion = analizar(frase)

    print(
        "Sujeto:",
        sujeto
    )

    print(
        "Acción:",
        accion
    )

    print()