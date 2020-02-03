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


    def zoom(self, xstart, xrange, ystart, yrange, scale):
        if(xstart*scale+xrange*scale > len(self.matrix) or ystart*scale + yrange*scale > len(self.matrix[0])):
            print("cant zoom bigger terrain than exist")
            return
        zoomline = []
        zoommatrix = []
        for x in range(0, xrange*scale):
            for y in range(0, yrange*scale):
                zoomline.append(self.matrix[xstart*scale + x][ystart*scale + y])
            zoommatrix.append(zoomline)
            zoomline = []
        Zrows = len(np.array(zoommatrix))
        Zcols = len(np.array(zoommatrix)[0])
        fig = go.Figure(data=[go.Surface(z=np.array(zoommatrix))])
        fig.update_layout(title='Zoom from x:'+str(xstart)+' to '+str(xrange*scale)+' and from y: '+str(ystart)+' to '+str(yrange*scale))
        fig.update_layout(
                scene = {
                    "xaxis": {"nticks": 1},
                    "zaxis": {"nticks": 1},
                    "aspectratio": {"x": Zrows, "y": Zcols, "z": 10}
                })
        fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
        fig.show()