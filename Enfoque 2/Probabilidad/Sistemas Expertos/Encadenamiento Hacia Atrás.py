hechos = [
    "llueve"
]

reglas = {
    "trafico": "llueve",
    "estres": "trafico",
    "tarde": "estres"
}

def verificar(meta):

    if meta in hechos:
        return True

    if meta not in reglas:
        return False

    condicion = reglas[meta]

    return verificar(condicion)

objetivo = "tarde"

resultado = verificar(objetivo)

print(
    "¿Se puede concluir",
    objetivo,
    "?",
    resultado
)