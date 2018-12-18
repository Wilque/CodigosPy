#***URI 1020*** -Calculo de dias para idade-
Idias = int(input())

anos = int()
meses = int()
dias = int()

while (Idias >= 0) and (Idias >=365): #Vendo qnts anos a pessoa tem
    Idias -=365
    anos +=1
while (Idias >= 0) and (Idias >=30):#Meses
    Idias -=30
    meses +=1
while (Idias != 0):#Dias
    Idias -=1
    dias +=1
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))
