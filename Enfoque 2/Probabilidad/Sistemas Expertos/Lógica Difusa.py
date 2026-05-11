temperatura = 35

def caliente(t):

    if t <= 20:
        return 0

    if t >= 40:
        return 1

    return (t - 20) / (40 - 20)

grado = caliente(temperatura)

print("Temperatura:", temperatura)

print(
    "Grado de caliente:",
    round(grado, 2)
)

if grado > 0.7:
    print("Ventilador: ALTO")

elif grado > 0.3:
    print("Ventilador: MEDIO")

else:
    print("Ventilador: BAJO")