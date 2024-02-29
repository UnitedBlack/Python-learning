import requests
import pandas as pd
from lxml import etree
import os

TRUSIKI = "http://stripmag.ru/cat.php?id=316&show=30"
PIZHAMKI = "http://stripmag.ru/cat.php?id=269&show=30"
VIBRATORI = "http://stripmag.ru/cat.php?id=3&show=30"


def get_product_specs(url):
    html = requests.get(url).text
    root = etree.HTML(html)
    product_page = ["https://stripmag.ru" + item for item in root.xpath('//tr/td[@align="LEFT"]/a//@href')]
    product_page_html = [requests.get(item).text for item in product_page]
    root_product_page = [etree.HTML(item) for item in product_page_html]
    
    product_price = [item.xpath('//b[@class="red"][1]/text()')[0] for item in root_product_page]
    product_name = [item.xpath('//h1[1]/text()[1]')[0] for item in root_product_page]
    return product_price, product_name
    
    
# price, name = get_product_specs(TRUSIKI)

df = pd.read_excel('output.xlsx', engine='openpyxl')

# Вывод первых 5 строк DataFrame
print(df.head())

# Изменение данных в DataFrame
df['hueta'] = df['hueta2'] * 2

# Запись DataFrame обратно в Excel
df.to_excel('output.xlsx', index=False)

# trusiki_html = requests.get(TRUSIKI).text
# pizhamki_html = requests.get(PIZHAMKI).text
# vibratori_html = requests.get(VIBRATORI).text

# root_trusiki = etree.HTML(trusiki_html)
# root_pizhamki = etree.HTML(pizhamki_html)
# root_vibratori = etree.HTML(vibratori_html)

# trusi_product_page = ["https://stripmag.ru" + trusiki for trusiki in root_trusiki.xpath('//tr/td[@align="LEFT"]/a//@href')]
# pizhamki_product_page = ["https://stripmag.ru" + pizhamki for pizhamki in root_pizhamki.xpath('//tr/td[@align="LEFT"]/a//@href')]
# vibratori_product_page = ["https://stripmag.ru" + vibratori for vibratori in root_vibratori.xpath('//tr/td[@align="LEFT"]/a//@href')]

# trusiki_product_page_html = [requests.get(item).text for item in trusi_product_page] 
# pizhamki_product_page_html = [requests.get(item).text for item in pizhamki_product_page] 
# vibratori_product_page_html = [requests.get(item).text for item in vibratori_product_page] 

# root_trusiki_pp = [etree.HTML(item) for item in trusiki_product_page_html]
# root_pizhamki_pp = etree.HTML(pizhamki_product_page_html)
# root_vibratori_pp = etree.HTML(vibratori_product_page_html)

# trusiki_price = [item.xpath('//b[@class="red"][1]/text()')[0] for item in root_trusiki_pp]
# pizhamki_price = root_pizhamki_pp.xpath('//b[@class="red"][1]/text()')[0]
# vibratori_price = root_vibratori_pp.xpath('//b[@class="red"][1]/text()')[0]

# trusiki_name = [item.xpath('//h1[1]/text()[1]')[0] for item in root_trusiki_pp]


# //h1[1]/text()[1] - название

# //td[@valign][2]/b/@class
# //b[@class="red"][1]/text()

"""
Артикул
Цена
НДС %
Вес
Ширина, высота, длина упаковки
Ссылка на пикчу
Бренд
Длина см
Тип

"""