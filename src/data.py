import math
import copy
from database import Database

class Data:
    # setup and read data from the provided filename
    def __init__(self, limit_total):
        # implementation specific details
        # currently using 7 dimensions
        self.data_start_index = 1
        self.data_end_index = 7
        self.limit_total = limit_total # number of samples

        # data structures for raw data, cleaned data and calculations
        self.data = [] # populated after read_data
        self.standardized_data = [] # populated after standardize_data
        self.distance_matrix = [] # populated after calculate_distance_matrix

        # data initialization
        self.read_data()
        self.standardize_data()
        self.calculate_distance_matrix()

    def read_data(self):
        db = Database()
        self.data = db.read_data(self.limit_total)
        db.close()

    # the length of the data set, assume all columns the same length
    def data_length(self):
        return len(self.data)

    # find the mean for a given column (attribute), assume there is a header so
    # skip the first iteration
    def attribute_mean(self, col_index):
        sum = 0
        for i in range(0, self.data_length()):
            try:
                sum += float(self.data[i][col_index])
            except:
                print str(i) + " " + str(col_index)

        # calculate the mean
        return sum / (self.data_length())

    # find the standard deviation for a given column (attribute)
    def standard_deviation(self, col_index, mean):
        sum = 0
        for i in range(0, self.data_length()):
            try:
                sum += math.pow(float(self.data[i][col_index]) - mean, 2)
            except:
                print str(i) + " " + str(col_index)
        return math.sqrt((1.0 / self.data_length()) * sum)

    # for the given column (attribute), standardize all of the data
    def standardize_column(self, col_index):
        mean = self.attribute_mean(col_index)
        standard_deviation = self.standard_deviation(col_index, mean)
        for i in range(0, self.data_length()):
            try:
                standardized = (float(self.data[i][col_index]) - mean) / standard_deviation
            except:
                print str(i) + " " + str(col_index)

            self.standardized_data[i][col_index] = standardized

    def standardize_data(self):
        # standardize columns 3 up to and including 7
        self.standardized_data = copy.deepcopy(self.data)
        for col_index in range(self.data_start_index, self.data_end_index + 1):
            self.standardize_column(col_index)

    # find the distance between two vectors of the same length using the
    # euclidean distance algorithm
    def euclidean_distance(self, vector_a, vector_b):
        sum = 0
        for i in range(0, len(vector_a)):
            sum += math.pow(vector_a[i] - vector_b[i], 2)
        return math.sqrt(sum)

    # generate a distance matrix between all songs
    def calculate_distance_matrix(self):
        for i in range(0, self.data_length()):
            self.distance_matrix.append([])
            for j in range(0, self.data_length()):
                dist = self.euclidean_distance(self.get_vector(i), self.get_vector(j))
                self.distance_matrix[i].append(dist)

    # get the distance between a data point index and an arbitrary vector
    def get_distance(self, index, vector):
        return self.euclidean_distance(self.get_vector(index), vector)

    # get the standardized vector given a data point index
    def get_vector(self, index):
        return self.standardized_data[index][self.data_start_index:self.data_end_index + 1]
