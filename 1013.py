#***URI 1013*** saber qual e o maior numero entre tres
num = input()#guardando os tres em unica linha
lisNum = []
lisNum = num.split(' ')#separando-os
a = lisNum[0]#usando individualmente
b = lisNum[1]
c = lisNum[2]
num1 = int(a)#agr sao int
num2 = int(b)
num3 = int(c)
maiorN1N2 = (num1+num2+abs(num1-num2))/2#operacao que descobre qual num e maior
maior = (maiorN1N2+num3+abs(maiorN1N2-num3))/2#comparando com o ultimo valor entrado
maior = int(maior)#transformando em int ja que ele fica como float
print(maior)
