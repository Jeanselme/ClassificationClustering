import matplotlib.pyplot as plt
import numpy as np

def plotCluster(cluster, parentPosition, number, totalNumberChild, width, colors):
    """
    Plots the current cluster
    Thanks to the position of the parent and the number of other children
    """
    # Computes the reparition of class in the cluster
    mean = cluster.labels.mean(axis=0)
    color = np.sum([mean[i]/mean.sum()* colors[i] for i in range(len(colors))], axis=0)

    # Computes and plots the position of the node
    currentPosition = parentPosition + [(width * number/(totalNumberChild-1)-width/2), 1]
    plt.plot([parentPosition[0], currentPosition[0]], [parentPosition[1], currentPosition[1]],
        color = color)

    # Calls over all children
    for c, i in zip(cluster.children, range(len(cluster.children))):
        plotCluster(c, currentPosition, i, len(cluster.children),
            width / totalNumberChild, colors)

def plotDendrogram(cluster, colors = None, labels = None):
    """
    Plot the dendrogram of the given clusters, adapt the color thanks to
    the repartition of data in the cluster
    """
    plt.figure("Dendrogram")
    ax = plt.gca()

    numberClass = len(cluster.labels[0])

    if colors is None or len(colors) != numberClass:
        # Create the same number of colors than classes
        colors = [np.random.rand(3) for i in range(numberClass)]

    if labels is None or len(labels) != len(colors):
        labels = [i + 1 for i in range(len(colors))]

    # Create legend
    ax.legend(loc="lower left", markerscale=0.7, scatterpoints=1, fontsize=10)

    # Plot the initial node and recurse
    plotCluster(cluster, np.array((0,0)), 1, 3, 100, colors)
    ax.set_ylabel("Depth")
    ax.invert_yaxis()
    ax.get_xaxis().set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    plt.show()
    plt.close()
