import re
import requests
import sys
from params import params, cookies, headers
from lxml import html
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
# from ui_form import Ui_Widget

vacancy_name_regexp = r"(\d+\.\s.*?),"
vacancy_url_regexp = r"\s(https:\/\/[\w\/.?=-]+)"

def description_parser(name_re=vacancy_name_regexp, url_re=vacancy_url_regexp):
    with open(f'Parsed-23-00.txt', 'r', encoding='utf-8') as file:
        for current_vacancy in file:
            regexped_name = re.search(name_re, current_vacancy).group()
            regexped_url = re.search(url_re, current_vacancy).group()
            response = requests.get(regexped_url, params=params, cookies=cookies, headers=headers)
            html_string = response.text
            root = html.fromstring(html_string)

            vacancy_main_title = " ".join(root.xpath('//h1[@data-qa="vacancy-title"]/text()'))
            vacancy_response_button_url = " ".join(root.xpath('//a[@data-qa="vacancy-response-link-top"]/@href'))
            vacancy_company_name = " ".join(root.xpath('//a[@data-qa="vacancy-company-name"]/span/text()'))
            vacancy_description = " ".join(root.xpath('//div[@data-qa="vacancy-description"]//text()'))

    return vacancy_response_button_url, vacancy_company_name, vacancy_description


        