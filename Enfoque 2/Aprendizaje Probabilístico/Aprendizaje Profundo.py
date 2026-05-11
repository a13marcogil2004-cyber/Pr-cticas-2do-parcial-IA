import math

X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

y = [0, 0, 0, 1]

w = [0.5, 0.5]
b = -0.7

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def predict(x):
    z = x[0]*w[0] + x[1]*w[1] + b
    return sigmoid(z)

for i in X:
    print(predict(i))