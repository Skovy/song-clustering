import numpy as np
import plotly
from data import Data
from plotly.tools import FigureFactory

class Dendrogram:
    def __init__(self, data):
        self.data = data # data source and basic computations
        self.names = [] # names of samples in order

        # populate data and create dendrogram
        self.generate_names()
        self.generate_dendrogram()

    # create the list of labels to apply to each sample
    def generate_names(self):
        for row in self.data.data:
            self.names.append(row[0])

    # create a dendrogram from the data and generate a HTML file
    def generate_dendrogram(self):
        x = np.array(self.data.distance_matrix)
        fig = FigureFactory.create_dendrogram(x, orientation='left', labels=self.names)
        fig['layout'].update({'width':1600, 'height':80000, 'margin': { 'l': 400 }})
        plotly.offline.plot(fig, filename='output/dendrogram.html')
