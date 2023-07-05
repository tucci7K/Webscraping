import requests
from bs4 import BeautifulSoup
#faz a requisição do link
pagina = requests.get('https://books.toscrape.com')

#buscar o conteudo da pagina em HTML
site = BeautifulSoup(pagina.content, 'html.parser') 

#procura a tag no site, e depois tem que instanciar dentro do produto "attrs"
produtos = site.find_all('article', attrs= {'class':'product_pod'})

#x é a variavel que estamos criando, e no colchete coloca oque quer pegar| para cada 'x'(h3) ele tras para mim
nomes = [x.find('h3').find('a').get('title') for x in produtos]

print(nomes)

