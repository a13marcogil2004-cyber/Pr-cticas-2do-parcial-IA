import numpy as np

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([[0], [1], [1], [0]])

W1 = np.random.randn(2, 2)
b1 = np.zeros((1, 2))

W2 = np.random.randn(2, 1)
b2 = np.zeros((1, 1))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

lr = 0.1

for _ in range(5000):
    h = sigmoid(np.dot(X, W1) + b1)
    out = sigmoid(np.dot(h, W2) + b2)

    error = y - out

    d_out = error * out * (1 - out)
    d_h = d_out.dot(W2.T) * h * (1 - h)

    W2 += h.T.dot(d_out) * lr
    b2 += np.sum(d_out, axis=0) * lr

    W1 += X.T.dot(d_h) * lr
    b1 += np.sum(d_h, axis=0) * lr

print(out)