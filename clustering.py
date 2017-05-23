import numpy as np

class cluster:
    """
    Defines what is a cluster
    """
    def __init__(self, points, labels, children):
        self.points = points
        self.labels = labels

        # Computes centroid of the cluster
        # Computes t
        self.centroid = np.mean(np.concatenate([child.centroid for child in children]), axis = 0).reshape((1,-1))
        self.children = children

        self.distance = 0

    def __add__(self, other):
        """
        Merges two clusters
        """
        result = cluster(np.concatenate((self.points, other.points)),
            np.concatenate((self.labels, other.labels)), [self, other])
        return result

    @classmethod
    def distanceEuclidean(cls, cluster1, cluster2):
        """
        Computes the euclidean distance between two clusters
        """
        return np.sqrt(np.sum((cluster1.centroid - cluster2.centroid)**2))

class singleton(cluster):
    """
    Single points structure
    """
    def __init__(self, point, label):
        self.points = point.reshape((1,-1))
        self.labels = label.reshape((1,-1))
        self.centroid = self.points
        self.children = []
        self.distance = 0


def hierarchicalCluster(data, labels):
    """
    Computes on the given data (data) which are labeled (2d array binary labels)
    (first dimension needs to be the same for these 2d arrays) a hierarchical clustering
    """
    clusters = [singleton(data[i], labels[i]) for i in range(len(data))]

    # TODO : Take advantage of the data previously computed
    while len(clusters) != 1:
        # Computes the distance matrix between clusters
        matrixDistance = np.zeros((len(clusters), len(clusters)))
        matrixDistance[:] = np.nan
        for i in range(len(clusters)):
            # +1 to avoid diagonal computation
            for j in range(i + 1, len(clusters)):
                # Computes the merging
                matrixDistance[i,j] = cluster.distanceEuclidean(clusters[i], clusters[j])
                matrixDistance[j,i] = matrixDistance[i,j]

        # By adding nan, min of the full superior matrix of the possible evolution
        indexMin = np.nanargmin(matrixDistance)
        i = indexMin // len(clusters)
        j = indexMin % len(clusters)

        # Merge the two closest clusters which are able to evolve
        # ie which has not encountred the stopRation criterion
        newCluster =  clusters[i] + clusters[j]
        newCluster.distance = matrixDistance[i,j]

        ### Update the new centroids by removing the two previous ones and
        ### adding the new one
        clusters = [clusters[k] for k in range(len(clusters)) if k not in [i,j] ]
        clusters.append(newCluster)

    return clusters

def selectionHierarchicalCluster(clusters, ratioMin = 0.9):
    """
    Takes all the computed clusters and select the one which have an higher ratio
    then ratioMin
    """
    resultClusters = []
    # While we have not found what we want computes the research
    while clusters != []:
        nextCluster = []
        for c in clusters:
            # Verify if the majority is upper than a given threhold
            if c.labels.mean(axis=0).max() < ratioMin:
                # Append children
                nextCluster += c.children
            else:
                # Add the clusters to the list
                resultClusters.append(c)
        clusters = nextCluster

    return resultClusters
