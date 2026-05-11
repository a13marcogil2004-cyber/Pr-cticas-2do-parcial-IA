mundo_actual = {
    "llueve": True,
    "trafico": True
}

def necesario(evento):

    return mundo_actual.get(evento, False)

def posible(evento):

    return evento in mundo_actual

evento = "llueve"

print(
    "Necesariamente:",
    necesario(evento)
)

print(
    "Posiblemente:",
    posible(evento)
)