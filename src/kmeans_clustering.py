import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_digits

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
##plt.show()

''' Expectation–maximization (E–M) is a powerful algorithm that comes up
in a variety of contexts within data science. k-means is a particularly
simple and easy-to-understand application of the algorithm, and we will
walk through it briefly here. In short, the expectation–maximization
approach here consists of the following procedure:
Guess some cluster centers Repeat until converged
E-Step: assign points to the nearest cluster center
M-Step: set the cluster centers to the mean Here the
"E-step" or "Expectation step" is so-named because it involves updating
our expectation of which cluster each point belongs to. The "M-step" or
"Maximization step" is so-named because it involves maximizing some
fitness function that defines the location of the cluster centers—in
this case, that maximization is accomplished by taking a simple mean of
the data in each cluster to find out the cluster centers.
'''


# k-means on digits data

digits = load_digits()
print('digits obj', dir(digits))
print(digits.data.shape)
print(digits.data[0])

kmeans = KMeans(n_clusters = 10)
kmeans.fit(digits.data)
print(len(kmeans.cluster_centers_) )
print(kmeans.cluster_centers_[0])
print(len(kmeans.cluster_centers_[0]))

##clusters = kmeans.fit_predict(digits.data)
##print('clusters obj', clusters)
##print('clusters len', len(clusters))
##print(set(clusters))

fig, ax = plt.subplots(2, 5, figsize=(8, 3))
centers = kmeans.cluster_centers_.reshape(10, 8, 8)
for axi, center in zip(ax.flat, centers):
    axi.set(xticks=[], yticks=[])
    axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)

plt.show()
