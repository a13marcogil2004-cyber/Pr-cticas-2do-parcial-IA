conocimiento = {
    "Juan": "estudia",
    "Ana": "no_estudia"
}

def aprender(persona):

    estado = conocimiento[persona]

    if estado == "estudia":
        return "aprueba"

    return "reprueba"

for persona in conocimiento:

    resultado = aprender(persona)

    print(
        persona,
        "->",
        resultado
    )