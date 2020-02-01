import math
import numpy as np
import plotly.graph_objects as go


class BitMap():
    def __init__(self, matrix):
        self.matrix = matrix

    def showwithscale(self, input_scalar):
        Zrows = len(self.matrix)
        Zcols = len(self.matrix[0])
        ii = math.ceil(Zcols/input_scalar)
        i_adjust = np.zeros((Zrows, ii*input_scalar - Zcols ), dtype=np.int64)
        self.matrix = np.append(self.matrix, i_adjust, axis=1)
        Zrows = len(self.matrix)
        Zcols = len(self.matrix[0])
        jj = math.ceil(Zrows/input_scalar)
        j_adjust = np.zeros((jj*input_scalar-Zrows, Zcols), dtype=np.int64)
        self.matrix = np.append(self.matrix, j_adjust, axis=0) 
        lineholder = []
        matrixholder = []
        finalmatrix = []
        for j in range(0, jj):
            for i in range(0, ii):
                for _j in range(0, input_scalar):
                    for _i in range(0, input_scalar):
                        lineholder.append(int(self.matrix[j*input_scalar+_j][i*input_scalar+_i]))
                    matrixholder.append(lineholder)
                    lineholder = []
                finalmatrix.append(np.mean(matrixholder))
                matrixholder = []
        fmatline = []
        fmat = []
        for x in finalmatrix:
            fmatline.append(x)
            if(len(fmatline)>=ii):
                fmat.append(fmatline)
                fmatline = []
        Zrows = len(np.array(fmat))
        Zcols = len(np.array(fmat)[0])
        fig = go.Figure(data=[go.Surface(z=np.array(fmat))])
        fig.update_layout(title='Scale 1:'+str(input_scalar))
        fig.update_layout(
                scene = {
                    "xaxis": {"nticks": 1},
                    "zaxis": {"nticks": 1},
                    "aspectratio": {"x": Zrows, "y": Zcols, "z": 10} # z = ? moze max - min ? 
                })
        fig.update_traces(contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))
        fig.show()
