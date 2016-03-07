from src.hierarchical import Dendrogram
from src.kmeans import KMeans
from src.data import Data
import sys

limit_total = 100 # default to 100 samples
k = 10 # default to 10 clusters
if len(sys.argv) > 1:
    limit_total = sys.argv[1]
if len(sys.argv) > 2:
    k = sys.argv[2]

print 'Creating a Dendrogram with ' + str(limit_total) + ' samples...'
d = Dendrogram(limit_total)

print 'Clustering with ' + str(limit_total) + ' samples and ' + str(k) + ' clusters...'
k = KMeans(Data(limit_total), k)
k.perform_clustering()
k.print_clusters()
