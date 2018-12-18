from math import sqrt
p1 = input()
p2 = input()
lisP1 = []
lisP2 = []
lisP1 = p1.split(' ')
lisP2 = p2.split(' ')
x1 = lisP1[0]
y1 = lisP1[1]
x2 = lisP2[0]
y2 = lisP2[1]
X1 = float(x1)
Y1 = float(y1)
X2 = float(x2)
Y2 = float(y2)
d = sqrt((X2-X1)**2+(Y2-Y1)**2)
print('{:.4f}'.format(d))
