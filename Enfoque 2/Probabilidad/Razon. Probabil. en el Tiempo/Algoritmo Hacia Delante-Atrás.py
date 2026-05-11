observaciones = [
    0.9,
    0.8,
    0.7
]

forward = []

prob = 1

for obs in observaciones:

    prob *= obs

    forward.append(prob)

backward = []

prob = 1

for obs in reversed(observaciones):

    prob *= obs

    backward.insert(0, prob)

print("Forward:")

for valor in forward:
    print(round(valor, 4))

print("\nBackward:")

for valor in backward:
    print(round(valor, 4))