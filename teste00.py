from PIL import Image
import requests

cat = requests.get('https://api.thecatapi.com/v1/images/search')
urlCat = cat['0']
img = image.open('urlCat')
erint(img)
