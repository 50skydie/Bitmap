import bitmap as bm

f = open('bitmap.txt', "r")
a = []
for x in f:
     a.append(x.strip().rstrip().split(' '))

m1 = bm.BitMap(a)
m1.scale(100, 1)