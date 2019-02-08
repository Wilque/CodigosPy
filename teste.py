import requests
from bs4 import BeautifulSoup

resposta = requests.get('https://tempo.cptec.inpe.br')
sopa = BeautifulSoup(resposta.text, "html.parser")
tempm = sopa.find('span', attrs={'class': 'temp-max text-center font-dados' })
tempb = sopa.find('div', attrs={'class': 'p-1 temp-min font-dados'})
tempM = tempm.text
tempB = tempb.text
print('Maior: {} Menor: {}'.format(tempM, tempB))
