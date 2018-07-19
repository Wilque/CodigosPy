from math import sqrt

print('Equação do segundo grau')

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = b**2-4*a*c

if delta < 0:
    print('O sistema de equações com A: {}, B: {} e C: {}, não resulta em raízes reais'.format(a, b, c))
else:
    x1 = (-b+sqrt(delta))/2*a
    x2 = (-b-sqrt(delta))/2*a
    if delta == 0:
        print('O sistema de equações com A: {}, B: {} e C: {}, resulta em raízes iguais sendo ela = {}'.format(a, b, c, x1))
    else:
        print('X1 = {}, X2 = {}'.format(x1, x2))
