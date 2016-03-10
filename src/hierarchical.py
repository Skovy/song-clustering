import numpy as np
import plotly
from data import Data
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF
from scipy.spatial.distance import pdist, squareform

class Dendrogram:
    def __init__(self, limit_total):
        self.data = Data(limit_total) # data source and basic computations
        self.limit_total = limit_total # number of samples
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
        fig = FF.create_dendrogram(x, orientation='left', labels=self.names)
        fig['layout'].update({'width': 1600, 'height': self.dendrogram_height(), 'margin': { 'l': 400 }})
        plotly.offline.plot(fig, filename='output/dendrogram.html')

    def dendrogram_height(self):
        return 40 * self.limit_total

class DendrogramHeatmap:
    def __init__(self, limit_total):
        self.data = Data(limit_total) # data source and basic computations
        self.limit_total = limit_total # number of samples
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
        labels = self.names
        x = np.array(self.data.distance_matrix)

        # Initialize figure by creating upper dendrogram
        figure = FF.create_dendrogram(x, orientation='bottom', labels=labels)
        for i in range(len(figure['data'])):
            figure['data'][i]['yaxis'] = 'y2'

        # Create Side Dendrogram
        dendro_side = FF.create_dendrogram(x, orientation='right')
        for i in range(len(dendro_side['data'])):
            dendro_side['data'][i]['xaxis'] = 'x2'

        # Add Side Dendrogram Data to Figure
        figure['data'].extend(dendro_side['data'])

        # Create Heatmap
        dendro_leaves = dendro_side['layout']['yaxis']['ticktext']
        dendro_leaves = list(map(int, dendro_leaves))
        data_dist = pdist(x)
        heat_data = squareform(data_dist)
        heat_data = heat_data[dendro_leaves,:]
        heat_data = heat_data[:,dendro_leaves]

        heatmap = go.Data([
            go.Heatmap(
                x = dendro_leaves,
                y = dendro_leaves,
                z = heat_data,
                colorscale = 'YIGnBu'
            )
        ])

        heatmap[0]['x'] = figure['layout']['xaxis']['tickvals']
        heatmap[0]['y'] = dendro_side['layout']['yaxis']['tickvals']

        # Add Heatmap Data to Figure
        figure['data'].extend(go.Data(heatmap))

        # Edit Layout
        figure['layout'].update({'width':1600, 'height':1600,
                                 'showlegend':False, 'hovermode': 'closest',
                                 'margin': { 'b': 400 }
                                 })

        # Edit xaxis
        figure['layout']['xaxis'].update({'domain': [.15, 1],
                                          'mirror': False,
                                          'showgrid': False,
                                          'showline': False,
                                          'zeroline': False,
                                          'ticks':""})
        # Edit xaxis2
        figure['layout'].update({'xaxis2': {'domain': [0, .15],
                                           'mirror': False,
                                           'showgrid': False,
                                           'showline': False,
                                           'zeroline': False,
                                           'showticklabels': False,
                                           'ticks':""}})

        # Edit yaxis
        figure['layout']['yaxis'].update({'domain': [0, .85],
                                          'mirror': False,
                                          'showgrid': False,
                                          'showline': False,
                                          'zeroline': False,
                                          'showticklabels': False,
                                          'ticks': ""})
        # Edit yaxis2
        figure['layout'].update({'yaxis2':{'domain':[.825, .975],
                                           'mirror': False,
                                           'showgrid': False,
                                           'showline': False,
                                           'zeroline': False,
                                           'showticklabels': False,
                                           'ticks':""}})

        # Plot!
        plotly.offline.plot(figure, filename='output/dendrogram_with_heatmap.html')
