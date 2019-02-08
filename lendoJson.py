import json
import requests

resposta = requests.get('https://api.thecatapi.com/v1/images/search').json()

imagem = resposta['url']
print(imagem)
