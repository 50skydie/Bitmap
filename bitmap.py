import math
import numpy as np
import plotly.graph_objects as go

class BitMap():
    def __init__(self, matrix):
        self.matrix = matrix

    def scale(self, scale, hsens):
        self.matrix = np.array(self.matrix)
        self.matrix = self.matrix.astype(int)
        rows = self.matrix.shape[0]
        cols = self.matrix.shape[1]
        returnmatrix = np.zeros((math.ceil(rows/scale),math.ceil(cols/scale)))
        for x in range(0, math.ceil(rows/scale)):
            for y in range(0, math.ceil(cols/scale)):
                returnmatrix[x][y] = np.mean(self.matrix[x*scale:(x+1)*scale,y*scale:(y+1)*scale])
        returnmatrix = returnmatrix.tolist()
        fig = go.Figure(data=[go.Surface(z=np.array(returnmatrix))])
        fig.update_layout(
                scene = {
                    "xaxis": {"nticks": 1},
                    "zaxis": {"nticks": 1},
                    "aspectratio": {"x": np.array(returnmatrix).shape[0], "y": np.array(returnmatrix).shape[1], "z": hsens}
                })
        fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
        fig.show()

    def zoom(self, xstart, xrange, ystart, yrange, scale, hsens):
        zoommatrix = np.array(self.matrix)[xstart*scale:xrange*scale+1, ystart*scale:yrange*scale+1]
        rows = zoommatrix.shape[0]
        cols = zoommatrix.shape[1]
        fig = go.Figure(data=[go.Surface(z=np.array(zoommatrix))])
        fig.update_layout(title='Zoom from x:'+str(xstart*scale)+' to '+str(xrange*scale)+' and from y: '+str(ystart*scale)+' to '+str(yrange*scale))
        fig.update_layout(
                scene = {
                    "xaxis": {"nticks": 1},
                    "zaxis": {"nticks": 1},
                    "aspectratio": {"x": rows, "y": cols, "z": hsens}
                })
        fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
        fig.show()