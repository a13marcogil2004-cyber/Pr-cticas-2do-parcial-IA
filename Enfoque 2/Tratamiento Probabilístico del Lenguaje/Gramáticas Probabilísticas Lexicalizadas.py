import random

grammar = {
    "S": [("NP(gato) VP(come)", 1.0)],
    "NP(gato)": [("el gato", 1.0)],
    "VP(come)": [("come NP(pescado)", 1.0)],
    "NP(pescado)": [("pescado", 1.0)]
}

def expand(symbol):
    if symbol not in grammar:
        return symbol

    rules = grammar[symbol]
    r = random.choices(rules, weights=[p for _, p in rules])[0]
    return " ".join(expand(s) for s in r[0].split())

print(expand("S"))