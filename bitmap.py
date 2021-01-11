import math
import numpy as np
import plotly.graph_objects as go
from PIL import Image

class BitMap():
    def __init__(self, matrix):
        self.matrix = matrix

    def scale(self, scale):
        self.matrix = np.array(self.matrix)
        self.matrix = self.matrix.astype(int)
        rows = self.matrix.shape[0]
        cols = self.matrix.shape[1]
        returnmatrix = np.zeros((math.ceil(rows/scale),math.ceil(cols/scale)))
        for x in range(0, math.ceil(rows/scale)):
            for y in range(0, math.ceil(cols/scale)):
                returnmatrix[x][y] = np.mean(self.matrix[x*scale:(x+1)*scale,y*scale:(y+1)*scale])
        self.matrix = returnmatrix.tolist()

    def cut(self, xstart, xrange, ystart, yrange):
        self.matrix = np.array(self.matrix)[xstart:xrange, ystart:yrange]

    def show(self, hsens):
        rows = np.array(self.matrix).shape[0]
        cols = np.array(self.matrix).shape[1]
        fig = go.Figure(data=[go.Surface(z=np.array(self.matrix))])
        fig.update_layout(
                scene = {
                    "xaxis": {"nticks": 1},
                    "zaxis": {"nticks": 1},
                    "aspectratio": {"x": rows, "y": cols, "z": hsens}
                })
        fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
        fig.show()

    def readBitmap(self, path):
        im = Image.open(path)
        rgb_im = im.convert('RGB')
        width, height = im.size
        output=np.zeros((width, height))
        strin2 = []
        for x in range(width):
            strin = []
            for y in range(height):
                output[x][y] = np.ceil(np.array(np.mean(rgb_im.getpixel((x, y)))))
                strin.append(output[x][y])
            strin2.append(strin)
        self.matrix = strin2