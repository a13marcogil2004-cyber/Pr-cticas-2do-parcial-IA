def utilidad(prob_exito, recompensa, costo):

    return (prob_exito * recompensa) - costo

sin_info = utilidad(
    prob_exito=0.5,
    recompensa=100,
    costo=0
)

con_info = utilidad(
    prob_exito=0.8,
    recompensa=100,
    costo=20
)

voi = con_info - sin_info

print("Utilidad sin información:", sin_info)
print("Utilidad con información:", con_info)
print("Valor de la información:", voi)