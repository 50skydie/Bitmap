import bitmap as bm

f = open('bitmap.txt', "r")
a = []
for x in f:
     a.append(x.strip().rstrip().split(' '))

m1 = bm.BitMap(a) #takes input
m1.showwithscale(50) #takes scale