import bitmap as bm

f = open('bitmap.txt', "r")
a = []
for x in f:
     a.append(x.strip().rstrip().split(' '))

#print(a)
m1 = bm.BitMap([0])
m1.readBitmap('bitmap.jpg')
m1.scale(1)
m1.show(20)