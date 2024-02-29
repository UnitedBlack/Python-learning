import lxml
from lxml import etree
from lxml import html
CYCLE_INDEX = 0
with open("index.html", "r", encoding="utf-8") as file:
    html_doc = file.read()

# print("Длина содержимого файла:", len(html_doc))

html_string = html_doc
root = html.fromstring(html_string)

xpath_vacancies_link = root.xpath(
    '//span[@data-page-analytics-event="vacancy_search_suitable_item"]//@href')
for i in xpath_vacancies_link:
    CYCLE_INDEX += 1
    print(CYCLE_INDEX, i)