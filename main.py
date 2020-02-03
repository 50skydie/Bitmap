import bitmap as bm

f = open('bitmap.txt', "r")
a = []
for x in f:
     a.append(x.strip().rstrip().split(' '))

m1 = bm.BitMap(a)
#m1.zoom(0,1,0,1,1)
m1.scale(100)