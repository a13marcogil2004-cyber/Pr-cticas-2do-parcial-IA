conocimiento = {
    "Perro": "Animal",
    "Animal": "SerVivo",
    "Gato": "Animal"
}

def inferir(objeto):

    actual = objeto

    while actual in conocimiento:

        siguiente = conocimiento[actual]

        print(
            actual,
            "->",
            siguiente
        )

        actual = siguiente

inferir("Perro")