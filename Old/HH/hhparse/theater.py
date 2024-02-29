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

data = [{'company_name': 'getmatch', 'salary': 'до 450\xa0000 ₽ на руки', 'vacancy_title': 'Python-разработчик', 'btn_response': '/applicant/vacancy_response?vacancyId=86120529&hhtmFrom=vacancy', 'vacancy_description': 'Ищем человека на позицию Python-разработчика для продуктовой IT-компании. Сейчас открыт поиск сразу в несколько проектов. У нас продуктовый и проектный подход к разработке - разработчики плотно общаются с продуктом, предлагают технические решения, отвечают за сходимость проектов. Есть реальная возможность влиять на то, что в итоге увидят пользователи, но требует большой самостоятельности и ответственности. Обязанности:  Участвовать в развитии и запуске продуктов на Python. Писать код на  Python, который легко читать, поддерживать и развивать. Выполнять задачи, связанные с масштабированием, оптимизацией и ускорением сервисов.   Требования:  От 3 лет коммерческого опыта на Python. Наличие высшего технического образования.  Условия:  Гибридный формат работы в РФ или релокация зарубеж. Профессиональное развитие: митапы, тренинги, мастер-классы, участие в конференциях. Расширенная программа ДМС: стоматология, обследования, вызов врача на дом и многое другое. Оплата 80% стоимости ДМС для супругов и детей. Компенсация обедов, фитнеса. '}, {'company_name': 'HFLabs', 'salary': 'от 200\xa0000 до 500\xa0000 ₽ на руки', 'vacancy_title': 'Робототехник (Robotics Engineer, Robotics Developer) с  опытом разработки на языке Python', 'btn_response': '/applicant/vacancy_response?vacancyId=86720535&hhtmFrom=vacancy', 'vacancy_description': 'Привет! Меня зовут Макс Серебро, я занимаюсь R&D направлением. Для одного из наших проектов ищу в свою команду инженера-разработчика с экспертизой в робототехнике. Это новый проект про разработку софта для беспилотной навигации коммунальной техники в Москве. Техника уже есть и работает, нужно разрабатывать на питоне алгоритмы беспилотной навигации для нее. Чем-то это похоже на алгоритмы для робота-пылесоса, но с особенностями — например, возможно, перед коммунальной техникой будет ездить дополнительный агрегат, убирающий с пути камни и крупные элементы, мешающие перемещению. Чем предстоит заниматься:  разрабатывать программную начинку робота для уборки улиц; построить релизный цикл; автоматизировать тестирование в симуляции для написанного кода; дорабатывать системы навигации и управления робота; корректировать среду симуляции для лучшего воспроизведения реального окружения; работать с компонентами робота; взаимодействовать с командой разработчиков партнеров производящих аппаратную платформу; готовить техническую документацию.  Каким мы видим нашего кандидата:  высшее техническое образование или самостоятельный бэкграунд в области робототехники и смежных областей; опыт разработки и проектирования робототехнических систем; владение английским языком на техническом уровне;  Плюсом будет:  высшее математическое образование, знание C++, понимание алгоритмов навигации, таких как SLAM (Simultaneous Localization and Mapping), A* (A-star), Dijkstra и других, знание алгоритмов и методов обработки изображений и видео, используемых для распознавания объектов, определения препятствий и планирования пути, опыт работы с данными от различных датчиков, таких как лидары, радары, инерциальные навигационные системы, GPS и камеры.  Технологический стек:  ROS 2 (galactic, humble); NAV 2; Gazebo; Python.  Что мы предлагаем:   конкурентную заработную плату и ее пересмотр минимум раз в год;   тихий и просторный офис в центре Москвы в двух минутах пешком от м. Парк культуры, возможен переезд в Сколково;   мощное железо для решения рабочих задач;   гибкое начало и окончание рабочего дня;   отсутствие бюрократии и горизонтальную структуру без десятка начальников;   команду единомышленников, с которой интересно не только работать, но и дружить, общаться, заниматься спортом, путешествовать.  '}, {'company_name': 'BostonGene Technologies', 'salary': 'от 5\xa0000 $ на руки', 'vacancy_title': 'Python Backend Team Lead (To Yerevan)', 'btn_response': '/applicant/vacancy_response?vacancyId=85051950&hhtmFrom=vacancy', 'vacancy_description': 'BostonGene - подуктовая BioTech компания, занимаемся разработкой облачной платформы, облегчающей врачу выбор терапии в лечении онкозаболеваний. Кого ищем и зачем?Ищем тимлида :) на команду из 8 человек. Задачи:  участие в проектировании архитектуры и сквозных интеграций со смежными сервисами. code review работа с командой (people management) управление процессами получения и груминга задач с командой и внутренним заказчиком  Стек на BE: Python 3.10/11, Flask/FastAPI, SQLAlchemy, Celery, PostgreSQL 14.7, Pytest, Микросервисная архитектура.На FE React+TS, писать на нём не надо, но желательно что-то поверхностно понимать. Требования:— оконченное высшее образование, желательно техническое— опыт ведения команды разработчиков от 3х лет— опыт написания сервисов на Python от 5 лет— глубокое понимание принципов ООП и архитектурных паттернов— готовность разбираться в сложной предметной области Будет плюсом, но необязательно:— минимальный опыт с FE на React.js— минимальное понимание или практический опыт с k8s— минимальные знания Java (соседние сервисы написаны на Java 19) Условия:— релокация успешного кандидата и его членов семьи (в том числе кошечек и собачек) в Ереван, Армению. Оплата проживания на первое время, помощь с поиском квартиры— полная информационная и юридическая поддержка (ВНЖ, банковские счета, поиск квартиры, консультации по образовательным учреждениям для детей и т.д.)— внутрикорпоративные обучающие курсы, корпоративный план в спортзал, курсы английского языка, курсы армянского языка— гибкий график работы (начало дня с 9:00 до 12:00) Этапы собеседований:HR (30 минут) => техническое собеседование (2 часа) => знакомство с Head of Development (1 час) => оффер \\ фидбек'}, {'company_name': 'HR СНАЙПЕР', 'salary': 'от 800\xa0000 до 1\xa0200\xa0000 ₽ на руки', 'vacancy_title': 'Chief Technology Officer/CTO', 'btn_response': '/applicant/vacancy_response?vacancyId=78157311&hhtmFrom=vacancy', 'vacancy_description': 'Компания,  которая разработала уникальное всемирное мобильное приложение, в котором пользователи могут монетизировать свой контент и любые действия, привычные для других соц.сетей! Какой стек используют. python: FastAPI, pytest, aiohttp REST API Postgresql, MongoDB, ClickHouse RabbitMQ, Kafka Docker AWS Kubernetes Prometheus, Grafana mypy, flake8, pylint, bandit, radon Gitlab CI/CD OpenAPI JIRA, Confluence   Обязанности:  Руководство подразделением (100 чел) Организация процессов от идеи до авторского надзора Контроль сроков и качества выполненных работ Организация, проведение совещаний Формирование проектной команды Проектирование/ архитектура Внедрение и оптимизация процессов Контроль за экономикой проектов Оптимизация всех бизнес процессов подразделения Проведение совещаний с ключевыми заказчиками Оценка технического долга Единая культура разработки Информация о компании: платформа коротких видео, где пользователи получают деньги за участие в челленджах (для пользователя -это возможность заработать, для блогера -инструмент привлечения новых лиц, для бренда- инструмент нативной рекламы)  Требования:  Образование – высшее Опыт работы в крупнейших мировых IT компаниях ( Google, Facebook, Microsoft, Amazon, Авито, Озон) Опыт работы в должности – более 5 лет Опыт работы руководителем (от 100 чел) Отличное понимание бизнес процессов компании Scrum, Jira  Условия:  Работайте, где удобно: офис, дом, берег Бали Конкурентные зарплаты + бенефиты и программа опционов (оклад оговаривается с каждым кандидатом индивидуально) Заработная плата растет вместе с уровнем твоих навыков Команда: работа бок о бок с крутыми специалистами из IT-индустрии со всего мира, каждый из которых готов поделиться своей экспертизой Техника: мощное железо, дополнительные мониторы, гаджеты и все, что позволит тебе работать максимально эффективно Сложные и интересные задачи в области высоконагруженных систем Профессиональное развитие: прямо в офисе мы организуем конференции, встречи разработчиков, семинары и тренинги, куда открыт доступ сотрудникам, обучение и повышение квалификации за счет компании Личностное развитие: наши  сотрудники делятся своей экспертизой как на внутренних образовательных порталах, так и участвуют во внешних конференциях Здоровая корпоративная культура: фитнес, йога, выездные мероприятия, в том числе и за рубеж;   '}]

if __name__ == "__main__":    
    HHEblya = HH()
    # HHEblya.load_page(from_who='auto', option=True, 
    # link="https://hh.ru/search/vacancy?area=1&search_field=name&search_field=company_name&search_field=description&enable_snippets=true&L_save_area=true&education=higher&industry=7&text=python&salary=450000&only_with_salary=true")
    app = QApplication(sys.argv)
    window = WindowMain(data)
    window.get_weather(api_key="e8c4e195e035f4befb6d2f044b5cfcc5")
    window.show()
    sys.exit(app.exec())
