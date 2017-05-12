# Clustering for labeled data

# Algorithm

## Hierarchical Clustering
First, execute a simple hierarchical clustering which merges clusters until it remains only one.
To do so it computes the distance between each centroids and merge the closest ones.

## Analysis of the dendrogram
From the previous step, we obtain a tree of clusters (dendrogram). The latter is usually cut at a given distance, which ensures a minimum distance between each cluster.
The adopted approach in this classification problem uses an other metric : the number of both category in the cluster. To do so, we define a minimum ratio number over all other classes in the cluster. This way each cluster is representative of a subpart of a category.
However both approach can be mixed in order to have meaningful clusters for both category with a minimum distance between each.

# Explanation
It is not envisageable to do both computation in the same time because by stopping the merging phase for some clusters, you can observe strange comportments.

# Example
The following figures are obtained thanks to the script example.py, which plots two gaussians (first image) and cluster them with a ratio of categories of 90\%.
![Gaussian](https://raw.githubusercontent.com/Jeanselme/ClassificationClustering/master/Images/gaussians.png)  ![Cluster](https://raw.githubusercontent.com/Jeanselme/ClassificationClustering/master/Images/clusters.png)  

# Dependencies
Executed with python3.5 with the library matplotlib and numpy.
