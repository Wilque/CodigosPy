import random

listaAlfabeto =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listaMaiuscula = []

for i in listaAlfabeto:
    listaMaiuscula.append(i.upper())

print(listaAlfabeto)
print(listaMaiuscula)

nome = ['witalo']
while nome != 'wilque':
    nome[0] = random.choice(listaAlfabeto)
    nome[1] = random.choice(listaAlfabeto)
    '''if nome[0] == nome[1]:
        while nome[1] == nome[0]:
            nome[1] = random.choice(listaAlfabeto)'''
         
    nome[2] = random.choice(listaAlfabeto)
    '''if nome[2] == nome[0] or nome[1] nome[2]:
        while nome[2] == nome[1] or nome[2] == nome[0]:
            nome[2] = random.choice(listaAlfabeto)'''

    nome[3] = random.choice(listaAlfabeto)
    '''if  nome[3] == nome[2] or nome[3] == nome[0] or nome[1] nome[2]:
        while nome[2] == nome[1] or nome[2] == nome[0]:
            nome[2] = random.choice(listaAlfabeto)'''
    
    nome[4] = random.choice(listaAlfabeto)
    nome[5] = random.choice(listaAlfabeto)
    print (nome)
    #letras = random.choice(listaAlfabeto)

print(letras)
