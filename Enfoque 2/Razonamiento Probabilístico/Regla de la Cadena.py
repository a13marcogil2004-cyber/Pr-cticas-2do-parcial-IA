p_lluvia = 0.3

p_trafico_dado_lluvia = 0.8

p_conjunta = (
    p_lluvia
    *
    p_trafico_dado_lluvia
)

print(
    "P(Lluvia y Tráfico):"
)

print(round(p_conjunta, 4))