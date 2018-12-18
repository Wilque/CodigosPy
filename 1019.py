#***URI-1019*** Convertendo segundos para H:M:S
N = int(input())

if (N >= 3600):#Vendo se o valor em s consegue completar 1H
    H = N/3600#dividi-se por 3600 para saber qnts H
    m = H %1#pegando parte do float apos o .
    H = H//1#pegando parte inteira do float
    m = m*60#temos aqui qnts m foram
    H = int(H)#passando a um int
    s = m%1#pegando parte apos o . dos m
    m = m//1#pegando parte inteira do m
    m = int(m)#transformando em int
    s = s*60
    s = int(s)
    print('{}:{}:{}'.format(H, m, s))
else:
    m = N/60
    s = m%1
    m = m//1
    s = s*60
    s = int(s)
    m = int(m)
    print('0:{}:{}'.format(m, s))
