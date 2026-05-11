import numpy as np

data = np.array([
    [0.1, 0.2],
    [0.2, 0.1],
    [0.8, 0.9],
    [0.9, 0.8]
])

grid_size = 2
weights = np.random.rand(grid_size, grid_size, 2)

lr = 0.5

def dist(a, b):
    return np.linalg.norm(a - b)

for _ in range(100):
    for x in data:
        bmu = (0, 0)
        min_dist = float("inf")

        for i in range(grid_size):
            for j in range(grid_size):
                d = dist(x, weights[i, j])
                if d < min_dist:
                    min_dist = d
                    bmu = (i, j)

        i, j = bmu
        weights[i, j] += lr * (x - weights[i, j])

print(weights)