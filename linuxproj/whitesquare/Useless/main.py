import requests
import lxml
from bs4 import BeautifulSoup as bs
import re
from Useless.forhttp import cookies
from Useless.forhttp import headers
from Useless.forhttp import params
from lxml import etree
from lxml import html

for_searching = "Маркетолог"
text_string = params['text'] = for_searching


def getting_html():
    response = requests.get('https://hh.ru/search/vacancy',
                            params=params, cookies=cookies, headers=headers)

    with open("index1.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    return response


response = getting_html()

html_string = response.text
root = html.fromstring(html_string)

parse = root.xpath(
    '//main[@class="vacancy-serp-content"]//span[@data-page-analytics-event="vacancy_search_suitable_item"]//@href')

for i, href in enumerate(parse, start=1):
    text_content = str(href)  # Получить текстовое содержимое текущего элемента
    print(f'{i}: {text_content}')

# # Выполняем XPath-запрос для получения значения элемента
# value = root.xpath('/root/element1/text()')
# print(value[0])  # Выводит "Value 1"

# soup = bs(response.content, 'html.parser')

# title = soup.find_all('a', class_="serp-item__title")

# for string in title:
#     current_string = string.text
#     print(current_string)
#     if current_string:
#         regexp = re.search(
#             r"(Python|python|junior python|Junior Python|junior Python|Junior python)", current_string)
#         print(regexp)

# get_respond_button = soup.find_all(
#     class_="bloko-button bloko-button_kind-success bloko-button_scale-small")


# Добавить отображение опыта
# Добавить логин(опциональный)
# Сделать фейковый аккаунт, сделать фейковое резюме с гпт
# Добавить функционал спама (отклика)
# Проспамить долбоебов
