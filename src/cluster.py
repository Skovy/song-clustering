class Cluster:
    def __init__(self, centroid_vector, data_set):
        self.data = [] # all of the data points in this cluster
        self.centroid_vector = centroid_vector
        self.data_set = data_set

    # add a value to the this cluster
    def assign_cluster(self, value):
        self.data.append(value)

    # remove a value from this cluster (if it exists)
    def remove(self, value):
        if value in self.data:
            self.data.remove(value)

    # provided with a centroid vector determine if there is a difference
    # with the current centroid
    def centroids_equal(self, new_centroid):
        for val in self.centroid_vector:
            if val not in new_centroid:
                return False
        return True

    # average all of the data to find the new centroid
    # returns if there was a change (true) or not (false)
    def recalculate_centroid(self):
        new_centroid = [0] * len(self.data_set.get_vector(0)) # TODO: find less jank way
        for data in self.data:
            for index, dimension in enumerate(self.data_set.get_vector(data)):
                new_centroid[index] += dimension

        for i in range(0, len(new_centroid)):
            new_centroid[i] = new_centroid[i] / len(self.data)
        equal = self.centroids_equal(new_centroid)
        self.centroid_vector = new_centroid
        return not equal
