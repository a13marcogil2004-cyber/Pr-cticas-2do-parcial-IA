import numpy as np

X = np.array([[0], [1]])
y = np.array([[0], [1]])

w = np.random.randn(1, 1)
b = 0
lr = 0.1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

for _ in range(1000):
    z = np.dot(X, w) + b
    y_pred = sigmoid(z)

    error = y - y_pred

    d = error * y_pred * (1 - y_pred)

    w += np.dot(X.T, d) * lr
    b += np.sum(d) * lr

print(y_pred)