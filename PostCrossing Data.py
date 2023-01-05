from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

df = pd.DataFrame(columns=["Pais destinatário","Tempo","Distancia","Envio","Chegada","ID"])
dados = []

def pegar_dados(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'lxml')

    if soup.find("i",{"class":"icn-mini r15"}) != None:
        tempo = soup.find("i",{"class":"icn-mini r15"}).next_sibling.text.replace("\n", "").replace("        ", "")
        distancia = soup.find("i", {"class": "icn-mini r4"}).next_sibling.text.replace("\n", "").replace("        ", "").replace("    ", "")
        pais_destinatario = soup.find_all('a',itemprop="addressCountry")[1].text
        envio = soup.find('time',itemprop="startTime").text
        chegada = soup.find('time',itemprop="endTime").text
        return [pais_destinatario,distancia,tempo,envio,chegada]

for i in range(5000):
    if pegar_dados(f"""https://www.postcrossing.com/postcards/NL-{5395682-i}""") != None:
        dados = pegar_dados(f"""https://www.postcrossing.com/postcards/NL-{5395682-i}""")
        dados.append(5395682 - i)
        df.loc[len(df)] = dados
    print(f"""{i}/5000""")
df.to_excel(r'C:\Users\danil\PycharmProjects\pythonProject\WebScrapping Study\DadosPostCrossing.xlsx', index=False)