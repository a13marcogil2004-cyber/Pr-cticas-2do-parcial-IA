import math

x = [1, 0, 1]
w = [0.4, -0.6, 0.8]
b = 0.1

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def neuron(x, w, b):
    z = 0
    for i in range(len(x)):
        z += x[i] * w[i]
    z += b
    return sigmoid(z)

print(neuron(x, w, b))