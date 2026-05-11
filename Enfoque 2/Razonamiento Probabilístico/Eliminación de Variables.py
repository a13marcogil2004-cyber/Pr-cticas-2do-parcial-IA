p_lluvia = 0.3

p_trafico_si_lluvia = 0.8

p_trafico_si_no_lluvia = 0.2

factor_lluvia = (
    p_lluvia
    *
    p_trafico_si_lluvia
)

factor_no_lluvia = (
    (1 - p_lluvia)
    *
    p_trafico_si_no_lluvia
)

prob_trafico = (
    factor_lluvia
    +
    factor_no_lluvia
)

print(
    "Probabilidad de tráfico:"
)

print(round(prob_trafico, 4))