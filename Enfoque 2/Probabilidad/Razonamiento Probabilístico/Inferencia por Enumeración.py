p_lluvia = 0.3

p_trafico_si_lluvia = 0.8

p_trafico_si_no_lluvia = 0.2

numerador = (
    p_trafico_si_lluvia
    *
    p_lluvia
)

denominador = (
    p_trafico_si_lluvia
    *
    p_lluvia
    +
    p_trafico_si_no_lluvia
    *
    (1 - p_lluvia)
)

resultado = numerador / denominador

print(
    "P(Lluvia | Tráfico):"
)

print(round(resultado, 4))