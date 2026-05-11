humanos = [
    "Juan",
    "Ana",
    "Carlos"
]

def humano(x):
    return x in humanos

def mortal(x):
    return humano(x)

for persona in humanos:

    if humano(persona):

        print(
            persona,
            "es mortal:",
            mortal(persona)
        )