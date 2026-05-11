import numpy as np
from sklearn.svm import SVC

X = np.array([
    [1, 2],
    [2, 3],
    [3, 3],
    [8, 8],
    [9, 8],
    [8, 9]
])

y = np.array([0, 0, 0, 1, 1, 1])

svm = SVC(kernel="linear")
svm.fit(X, y)

print(svm.predict([[2, 2]]))
print(svm.predict([[9, 9]]))