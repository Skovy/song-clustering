from src.hierarchical import Dendrogram, DendrogramHeatmap
from src.kmeans import KMeans
from src.data import Data
import sys

limit_total = 100 # default to 100 samples
k = 10 # default to 10 clusters
if len(sys.argv) > 1:
    limit_total = int(sys.argv[1])
if len(sys.argv) > 2:
    k = int(sys.argv[2])

print 'Clustering with ' + str(limit_total) + ' samples and ' + str(k) + ' clusters...'
k = KMeans(Data(limit_total), k)
k.perform_clustering()
k.print_clusters()

print 'Creating a Dendrogram with ' + str(limit_total) + ' samples...'
d = Dendrogram(limit_total)

print 'Creating a Dendrogram Heatmap with ' + str(limit_total) + ' samples...'
dh = DendrogramHeatmap(limit_total)
