import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def tanh(x):
    return math.tanh(x)

def relu(x):
    return max(0, x)

def leaky_relu(x):
    return x if x > 0 else 0.01 * x

values = [-3, -1, 0, 1, 3]

for x in values:
    print(x, sigmoid(x), tanh(x), relu(x), leaky_relu(x))