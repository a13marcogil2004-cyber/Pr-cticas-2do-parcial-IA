prob_lluvia = 0.3

prob_trafico_si_lluvia = 0.8

prob_trafico_si_no_lluvia = 0.2

prob_trafico = (
    prob_trafico_si_lluvia * prob_lluvia
    +
    prob_trafico_si_no_lluvia * (1 - prob_lluvia)
)

prob_lluvia_dado_trafico = (
    prob_trafico_si_lluvia * prob_lluvia
) / prob_trafico

print("Probabilidad de tráfico:")
print(round(prob_trafico, 4))

print("Probabilidad de lluvia dado tráfico:")
print(round(prob_lluvia_dado_trafico, 4))