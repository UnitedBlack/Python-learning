import sys # это хуйня чтобы управлять системой, окнами, файлами, папками итд
import time
import requests
import asyncio # эта хуйня чтобы управлять асинх функциями, если будешь юзать playwright async_api то тебе браузер
# нужно будет запускать через asyncio.run(бравзер)
import PySide6.QtCore # это ядро гуи
from datetime import datetime # это чтобы взять время из системы
from playwright.sync_api import sync_playwright # импорт функции бравзера sync значит дебилия, есть async
from typing import Optional
from PySide6.QtWidgets import QApplication, QMainWindow # это окно гуи (ПРЯМ ОКНО) и модули(QLabelText...)
from icons.main_ui import Ui_MainWindow

class HH():
    # типа якобы ты запускаешь класс, и вот эта хуйня innit? запускается первой (иниц.) и задает переменные со значениями на весь класс
    def __init__(self): # функция конструктор, глупая хуйня, можно не юзать, но долбоебы гики ее юзают, забей просто подчиняйся
        super(HH, self).__init__() # тоже глупая хуйня которая якобы типа наделает правами суперкласса нахуя не понятно тоже просто подчиняйся
        self.time = datetime.now().strftime("%H_%M") 
        self.cycle = 0
        self.data_dict_list = []
        self.data_keys = ['company_name', 'salary', 'vacancy_title', 'btn_response', 'vacancy_description']

# !!!задание егора пидарака добавить иф елсе чтобы если оно не видит попапа чтоб оно забивало хуй
    def respond(self, url, text=""): # отклик на вакансию
        self.page.goto(url, wait_until="domcontentloaded")
                                                                                            

      
    def __vacancy_body_parser(self, vacancy_url_list: list):
        print("Parsing bodies")
        
        for links in vacancy_url_list:
            self.page.goto(links, wait_until="domcontentloaded")
            
            try:
                self.company_name = self.page.query_selector('span[data-qa="bloko-header-2"]').text_content()
            except(AttributeError): 
                time.sleep(2)
                self.company_name = self.page.query_selector('span[data-qa="bloko-header-2"]').text_content()
                
            self.salary = self.page.query_selector('span[class="bloko-header-section-2 bloko-header-section-2_lite"]').text_content()
            self.vacancy_title = self.page.query_selector('h1[data-qa="vacancy-title"]').text_content()
            self.btn_response = self.page.query_selector('a[data-qa="vacancy-response-link-top"]').get_attribute('href')
            self.vacancy_description = self.page.query_selector('div[data-qa="vacancy-description"]').text_content()
            dictionary = dict(zip(self.data_keys,
                        [self.company_name, self.salary, self.vacancy_title, self.btn_response, self.vacancy_description]))

            self.data_dict_list.append(dictionary)

        
    def __vacancy_parser(self): # поебаться с названием адекватным
        print("Parsing main page")
        time.sleep(2) # change to wait for element
        btn_next_is_visible = self.page.is_visible("a[data-qa='pager-next']")
        self.list_link_vacancies = []
        
        while self.page.is_visible("a[data-qa='pager-next']"):
            btn_next_link = self.page.query_selector("a[data-qa='pager-next']").get_attribute('href')
            self.page.evaluate('(element) => { element.scrollIntoView(); }', self.page.query_selector("a[data-qa='pager-next']"))  # js код для скролла к кнопке дальше
            link_vacancy = self.page.query_selector_all("a[class='serp-item__title']")
            
            for links in link_vacancy:
                url = links.get_attribute("href")
                self.list_link_vacancies.append(url)

            self.page.goto(f"https://hh.ru{btn_next_link}", wait_until="domcontentloaded")
            
        else:
            link_vacancy = self.page.query_selector_all("a[class='serp-item__title']") # подрочиться с href в одну строку и селектор нормальный сделать
            for links in link_vacancy: 
                url = links.get_attribute("href")
                self.list_link_vacancies.append(url)

        self.__vacancy_body_parser(vacancy_url_list=self.list_link_vacancies)


    def __login(self):
            self.page.goto("https://hh.ru/account/login?backurl=%2F&hhtmFrom=main", wait_until="domcontentloaded")
            self.page.query_selector('button[data-qa="expand-login-by-password"]').click()
            self.page.query_selector('input[data-qa="login-input-username"]').fill('79771294588')
            self.page.query_selector('input[data-qa="login-input-password"]').fill('Bibaboba1!')
            self.page.query_selector('button[data-qa="account-login-submit"]').click()
            time.sleep(2)
    
    def load_page(self,from_who,link: str, option=False, text=""): # first function
        with sync_playwright() as playwright: # чтобы не закрывать бравзер можно юзать так
            browser = playwright.firefox.launch(headless=False) # экземпляр бравзера с параметром чтобы вылезало окно
            self.context = browser.new_context() # создание "нового профиля", сюда можно передавать куки итд
            self.page = self.context.new_page()
            self.__login()

            print("Loading page")
            if from_who == "button":
                self.respond(link, text)
            else: 
                self.page.goto(link, wait_until="domcontentloaded") # загрузка страницы с параметром ожидания когда загрузится разметка
                self.__vacancy_parser() # вызов другой функции

class WindowMain(QMainWindow):
    def __init__(self, hh_data:list):
        super(WindowMain, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.hh = HH()
        self.hh_data = hh_data 
        self.current_index = 0 
        self.previous_index = -1
        
        self.ui.btn_next.clicked.connect(self.__show_next_data)  # Связываем кнопку с методом
        self.ui.btn_prev.clicked.connect(self.__show_previous_data)  # Связываем кнопку для перехода назад
        self.ui.btn_respond.clicked.connect(self.__respond)
        
    def __respond(self):
        self.ui.textBrowser.setText("Откликнулся")
        text_edit_field = self.ui.edit_text.toPlainText()
        self.hh.load_page(from_who="button",link="https://hh.ru/applicant/vacancy_response?vacancyId=86324076&hhtmFrom=vacancy_search_list", text=text_edit_field)
        

    def __show_previous_data(self):
        if self.current_index > 0:
            self.current_index -= 1
            data = self.hh_data[self.current_index]
            self.__update_data(data)
            

    def __update_data(self, data):
        self.ui.company_name_text.setText(data['company_name'])
        self.ui.textBrowser.setText(data['vacancy_title'] + '\n' + data['vacancy_description'])
        self.ui.salary_text.setText(data['salary'])
        # self.ui.btn_respond.clicked.connect(self.__respond_to_vacancy(self.data)) # btn_prev = btn_response)) btn_backward eto knopka prev
        
        
    def __show_next_data(self):
        if self.current_index < len(self.hh_data) - 1:
            self.current_index += 1
            data = self.hh_data[self.current_index]
            self.__update_data(data)
        else:
            self.ui.company_name_text.setText("No more data")
            self.ui.textBrowser.setText("No more data")
            self.ui.salary_text.setText("No more data")


    def get_weather(self, api_key:str, city="Москва"):
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
        self.city = city
        data = response.json()
        main_data = data["main"]
        self.temperature = int(main_data["temp"])
        self.ui.weather_text.setText(f"{self.city} +{self.temperature}°C")
        self.__show_next_data()



if __name__ == "__main__":    
    HHEblya = HH()
    # HHEblya.load_page(from_who='auto', option=True, 
    # link="https://hh.ru/search/vacancy?area=1&search_field=name&search_field=company_name&search_field=description&enable_snippets=true&L_save_area=true&education=higher&industry=7&text=python&salary=450000&only_with_salary=true")
    app = QApplication(sys.argv)
    window = WindowMain(HHEblya.data_dict_list)
    window.get_weather(api_key="e8c4e195e035f4befb6d2f044b5cfcc5")
    window.show()
    sys.exit(app.exec())
