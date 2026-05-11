prob_lluvia = 0.3

prob_trafico_si_lluvia = 0.8

prob_trafico_si_no_lluvia = 0.2

def inferencia(trafico):

    if trafico:

        numerador = (
            prob_trafico_si_lluvia
            *
            prob_lluvia
        )

        denominador = (
            prob_trafico_si_lluvia
            *
            prob_lluvia
            +
            prob_trafico_si_no_lluvia
            *
            (1 - prob_lluvia)
        )

    else:

        numerador = (
            (1 - prob_trafico_si_lluvia)
            *
            prob_lluvia
        )

        denominador = (
            (1 - prob_trafico_si_lluvia)
            *
            prob_lluvia
            +
            (1 - prob_trafico_si_no_lluvia)
            *
            (1 - prob_lluvia)
        )

    return numerador / denominador

resultado = inferencia(True)

print(
    "P(Lluvia | Tráfico):"
)

print(round(resultado, 4))