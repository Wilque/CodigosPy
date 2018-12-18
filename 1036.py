from math import sqrt

val = input()
lisVal = []
lisVal = val.split(' ')
a = lisVal[0]
b = lisVal[1]
c = lisVal[2]
a = float(a)
b = float(b)
c = float(c)
delta = float()
delta = (b**2)-4*a*c
if (a == 0) or (delta < 0) :
    print('Impossivel calcular')
else:
    print(delta)
    x1 = (-b-sqrt(delta))/(2*a)
    x2 = (-b+sqrt(delta))/(2*a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))
