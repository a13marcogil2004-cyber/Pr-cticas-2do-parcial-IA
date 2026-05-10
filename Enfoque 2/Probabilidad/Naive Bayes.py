from collections import defaultdict

datos = [
    ("gratis oferta dinero", "spam"),
    ("gana dinero ahora", "spam"),
    ("hola como estas", "normal"),
    ("vamos a estudiar", "normal")
]

frecuencias = {
    "spam": defaultdict(int),
    "normal": defaultdict(int)
}

conteo_clases = {
    "spam": 0,
    "normal": 0
}

for texto, clase in datos:

    conteo_clases[clase] += 1

    palabras = texto.split()

    for palabra in palabras:
        frecuencias[clase][palabra] += 1

def clasificar(texto):

    palabras = texto.split()

    probabilidades = {}

    total = sum(conteo_clases.values())

    for clase in conteo_clases:

        prob = conteo_clases[clase] / total

        for palabra in palabras:

            prob *= (
                frecuencias[clase][palabra] + 1
            ) / (
                sum(frecuencias[clase].values()) + 1
            )

        probabilidades[clase] = prob

    return max(
        probabilidades,
        key=probabilidades.get
    )

mensaje = "gana dinero gratis"

resultado = clasificar(mensaje)

print("Clasificación:", resultado)