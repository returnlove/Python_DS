import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans


X, y_true = make_blobs(n_samples = 300, centers = 4, cluster_std = 0.60, random_state = 0)
##print(X[:5])
##print(y_true[:5])
plt.scatter(X[:,0],X[:,1])
##plt.show()


kmeans = KMeans(n_clusters = 4)
kmeans.fit(X)
y_pred = kmeans.predict(X)
print('cluster centers: ',kmeans.cluster_centers_)
centers = kmeans.cluster_centers_

plt.scatter(X[:,0], X[:,1], c = y_pred)
plt.scatter(centers[:,0], centers[:,1], c = 'black', s = 100)
plt.show()

