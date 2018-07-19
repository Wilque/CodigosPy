from random import randint

print('TentativasDeAdivinharNumeros')

num = int(input('Digite um numero entre 0 e 10000: '))
listachutes = []
verificapares = []
chute = randint(0, 10000)

while chute != num:
    chute = randint(0, 10000)
    if chute in listachutes:
        chute = randint(0, 10000)
    else:
        listachutes.append(chute)
    

print(listachutes)
print(len(listachutes))

for i in listachutes:
    if i not in verificapares:
        verificapares.append(i)
if len(verificapares) == len(listachutes):
    print('Tudo OK!!!')
else:
    print('Vai dormir')
    
