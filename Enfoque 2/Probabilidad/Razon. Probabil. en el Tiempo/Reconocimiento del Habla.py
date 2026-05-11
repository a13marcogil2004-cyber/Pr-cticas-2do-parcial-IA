audio = [
    0.2,
    0.5,
    0.8,
    0.1
]

if max(audio) > 0.7:

    palabra = "Hola"

else:

    palabra = "Desconocido"

print("Palabra detectada:")

print(palabra)