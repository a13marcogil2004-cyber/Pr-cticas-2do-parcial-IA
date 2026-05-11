import numpy as np
from sklearn.svm import SVC

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 0])

model = SVC(kernel="linear")
model.fit(X, y)

print(model.score(X, y))