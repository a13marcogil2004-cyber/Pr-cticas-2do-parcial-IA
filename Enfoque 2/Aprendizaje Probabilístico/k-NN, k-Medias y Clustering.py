import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

X = np.array([
    [1, 2],
    [2, 3],
    [3, 3],
    [8, 8],
    [9, 8],
    [8, 9]
])

y = np.array([0, 0, 0, 1, 1, 1])

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

print(knn.predict([[2, 2]]))

kmeans = KMeans(n_clusters=2, random_state=0, n_init=10)
kmeans.fit(X)

print(kmeans.labels_)
print(kmeans.cluster_centers_)