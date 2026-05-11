import random

grammar = {
    "S": [("NP VP", 1.0)],
    "NP": [("Det N", 0.6), ("N", 0.4)],
    "VP": [("V NP", 0.7), ("V", 0.3)],
    "Det": [("el", 1.0)],
    "N": [("gato", 0.5), ("perro", 0.5)],
    "V": [("come", 1.0)]
}

def expand(symbol):
    if symbol not in grammar:
        return symbol

    rules = grammar[symbol]
    r = random.choices(rules, weights=[p for _, p in rules])[0]
    return " ".join(expand(s) for s in r[0].split())

for _ in range(5):
    print(expand("S"))