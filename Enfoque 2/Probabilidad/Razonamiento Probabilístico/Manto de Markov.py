red = {
    "Lluvia": {
        "padres": [],
        "hijos": ["Trafico"]
    },

    "Trafico": {
        "padres": ["Lluvia"],
        "hijos": ["Retraso"]
    },

    "Retraso": {
        "padres": ["Trafico"],
        "hijos": []
    }
}

def manto_markov(nodo):

    padres = red[nodo]["padres"]

    hijos = red[nodo]["hijos"]

    padres_hijos = []

    for hijo in hijos:

        padres_hijos.extend(
            red[hijo]["padres"]
        )

    blanket = set(
        padres
        +
        hijos
        +
        padres_hijos
    )

    blanket.discard(nodo)

    return blanket

resultado = manto_markov("Trafico")

print("Manto de Markov:")

for nodo in resultado:
    print("-", nodo)