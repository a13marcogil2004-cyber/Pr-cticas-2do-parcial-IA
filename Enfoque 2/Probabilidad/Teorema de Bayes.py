def bayes(p_b_a, p_a, p_b):

    return (p_b_a * p_a) / p_b

p_enfermedad = 0.01

p_positivo_si_enfermo = 0.95

p_positivo = 0.10

resultado = bayes(
    p_positivo_si_enfermo,
    p_enfermedad,
    p_positivo
)

print("Probabilidad de enfermedad dado positivo:")
print(round(resultado, 4))