#***URI 1010*** calculo de compra
c1 = input()#compra 1
c2 = input()#compra 2
lisC1 = []
lisC2 = []
lisC1 = c1.split(' ')#passando a string cortada a uma lista
lisC2 = c2.split(' ')
codP1 = lisC1[0]#usando os dados agora por unidade
nP1 = lisC1[1]#num de pecas 1
vP1 = lisC1[2]#valor do produto 1
codP2 = lisC2[0]
nP2 = lisC2[1]
vP2 = lisC2[2]
NP1 = int(nP1)#tranformando-os em outro tipo para serem usados
VP1 = float(vP1)
NP2 = int(nP2)
VP2 = float(vP2)
ValorPago = NP1*VP1 + NP2*VP2#calculo da compra
print('VALOR A PAGAR: R$ {:.2f}'.format(ValorPago))
