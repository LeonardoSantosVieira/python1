import requests
from bs4 import BeautifulSoup

url = "https://www.pensador.com/tecnologia/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

resposta = requests.get(url, headers=headers)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, 'html.parser')

    # NOVA forma de pegar as frases
    frases = soup.find_all('p')

    print("Frases de tecnologia:\n")

    for frase in frases:
        texto = frase.get_text(strip=True)

        # filtrar textos maiores (evita menu, etc)
        if len(texto) > 50:
            print("-", texto)

else:
    print("Erro ao acessar o site.")