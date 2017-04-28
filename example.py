from clustering import hierarchicalCluster

import matplotlib.pyplot as plt
import numpy as np

numberPoint = 50

# Generates random gaussians
cov = [[1, 0], [0, 1]]

xg1, yg1 = np.random.multivariate_normal([0, 0], cov, numberPoint).T
xg2, yg2 = np.random.multivariate_normal([2, 2], cov, numberPoint).T

# Plots the data
plt.figure("Random points")
plt.scatter(xg1, yg1, color="blue")
plt.scatter(xg2, yg2, color="red")


# Data
data = np.zeros((numberPoint*2, 2))
data[:,0],data[:,1] = np.concatenate((xg1, xg2)), np.concatenate((yg1, yg2))
label = np.concatenate(([[1,0]]*numberPoint, [[0,1]]*numberPoint))

# Clusters them
clusters = hierarchicalCluster(data, label)
plt.figure("Clusters")
for c in clusters:
    plt.scatter(c.points[:,0], c.points[:,1])
plt.show()
