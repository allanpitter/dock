#dock21
#importa o modulo urlopen
'''
#Ex1 - Retornar o código html da página
from urllib.request import urlopen
url = "https://github.com"
pagina = urlopen(url)
html = pagina.read().decode("utf-8")
print(html)
'''
'''
#importar a biblioteca
import mechanicalsoup
# Metodo que aciona o Browser
browser = mechanicalsoup.Browser()
# Criar/Definir a url que tera a interação
url = "http://olympus.realpython.org/login"
pagina = browser.get(url)
print(pagina.soup)
'''
#Ex3 - Enviando parametros (usuario e senha)
#1 - Importar Biblioteca
import mechanicalsoup
#2 - Informações da navegação
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup
#3 - Campos do Formulario
form = login_html.select("form")[0]
form.select("input")[0]["value"]="zeus"
form.select("input")[1]["value"]="ThunderDude"
#4 - Enviar os dados
profile_page = browser.submit(form,login_page.url)
profile_page.url
#5 - Exibir em tela os link
links = profile_page.soup.select("a")
for link in links:
    address = link['href']
    text = link.text
    print(text,address)
