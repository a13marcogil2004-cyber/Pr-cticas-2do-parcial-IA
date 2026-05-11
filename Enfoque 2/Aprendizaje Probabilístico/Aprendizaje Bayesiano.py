prior = 0.4

likelihood = 0.8

evidencia = 0.5

posterior = (
    likelihood
    *
    prior
) / evidencia

print("Probabilidad posterior:")

print(round(posterior, 4))