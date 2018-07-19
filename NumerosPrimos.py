print('numeros primos entre 0 e 100')

numerosprimos = []
numerosimpares = []
contdiv = int(0)

for i in range(0, 101):
    print(i)
    if i%2 == 1:
        numerosimpares.append(i)
del numerosimpares[0]
numerosimpares.insert(0, 2)
print(numerosimpares)
for i in numerosimpares:
    print(i)
    for primo in range(i, 1):
        div = i%primo
        if div == 0:
            contdiv +=1
        if contdiv == 2:
            numerosprimos.append(i)
print(numerosprimos)
