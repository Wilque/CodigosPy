#***URI 1035*** calculo basico testando condicionais simples
val = input()#valores de entrada 4 int
lisVal = []
lisVal = val.split(' ')#colocando os valores em lista, pois sao dados em unica linha
a = lisVal[0]#Pegando os valores da lista e transformando-os em strings individuais
b = lisVal[1]
c = lisVal[2]
d = lisVal[3]
A = int(a)#Agora transforma-os em int, para testar a condicional
B = int(b)
C = int(c)
D = int(d)
if (B > C) and (D > A) and (C+D > A+B) and (C > 0) and (D > 0) and (A%2 == 0):#Condicional
    print('Valores aceitos')
else:#Nao satisfazendo as condicoes.
    print('Valores nao aceitos')
