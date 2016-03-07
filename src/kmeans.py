import math
from cluster import Cluster

class KMeans:
    # provide the data set (inherit from Data) and the number of clusters (k)
    def __init__(self, data_set, k):
        self.k = k
        self.data_set = data_set
        self.clusters = []

    # perform the clustering on the data with 'k' clusters
    def perform_clustering(self):
        self.initialize_clusters()
        self.iterate()

    # choose 'k' random centroids (forgy) and create corresponding clusters
    def initialize_clusters(self):
        # TODO: replace with random - currently using first k as centroids
        for i in range(0, self.k):
            self.clusters.append(Cluster(self.data_set.get_vector(i), self.data_set))
        self.assign_closest_clusters() # initial assignments

    # perform another iteration in clustering, for small data sets the number
    # of iterations should be very small and will break from the iteration but
    # set an upperbound for very large datasets
    def iterate(self):
        for i in range(0, 1000):
            change = self.recalculate_centroids()
            # stop if none of the cluster centroids changed
            if not change:
                break
            self.assign_closest_clusters()

    # debugging method, print the current cluster's data
    def print_clusters(self):
        print ''
        for c in self.clusters:
            res = '['
            for index in c.data:
                res += ' "' + self.data_set.data[index][0] + '"'
            print res + ' ]'

    # calculate the centroids for each cluster averaging all of the data points
    # currently in that cluster to find the new centroid (if it changes)
    def recalculate_centroids(self):
        clusters_change = False
        for cluster in self.clusters:
            change = cluster.recalculate_centroid()
            # only one cluster needs to change to continue iterating
            if change:
                clusters_change = True
        return clusters_change

    # find the closest cluster for a specific data point
    def assign_closest_clusters(self):
        # assign each data point to the closest cluster
        for i in range(0, self.data_set.data_length() - 1):
            min_val = 100000 # assuming standardized data - should be big enough
            min_cluster = None
            # find the cluster that is closest
            for cluster in self.clusters:
                dist = self.data_set.get_distance(i, cluster.centroid_vector)
                if dist < min_val:
                    min_val = dist
                    min_cluster = cluster

                # remove from all clusters (data may move between clusters)
                cluster.remove(i)

            # add the data point to the closest cluster
            min_cluster.assign_cluster(i)

    # calculate the within cluster sum of squares for all data points
    def within_cluster_sum_of_squares(self):
        wcss = 0
        for cluster in self.clusters:
            for data in cluster.data:
                dist = self.data_set.get_distance(data, cluster.centroid_vector)
                wcss += math.pow(dist, 2)
        return math.log(wcss)
