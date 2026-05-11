datos = [
    1,
    2,
    3,
    10,
    11,
    12
]

grupo_1 = []

grupo_2 = []

for dato in datos:

    if dato < 6:

        grupo_1.append(dato)

    else:

        grupo_2.append(dato)

print("Grupo 1:")

print(grupo_1)

print("\nGrupo 2:")

print(grupo_2)