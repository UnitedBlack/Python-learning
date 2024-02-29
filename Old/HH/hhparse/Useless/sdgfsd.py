vacancy = []

keys = ['company_name', 'salary', 'vacancy_title', 'vacancy_description', 'respond_url']

company_name = "MTS"
vacancy_description = "Очень крутая вакансия"
salary = "мешок зерна"
vacancy_title = "Уборщик"
respond_url = "https://sdgasdgasd.ru"

dictionary = dict(zip(keys, [company_name, salary, vacancy_title, vacancy_description, respond_url]))

company_name = "123"
vacancy_description = "Очень 234 вакансия"
salary = "мешок 234"
vacancy_title = "234"
respond_url = "https://sdg2342asdgasd.ru"

dictionary_2 = dict(zip(keys, [company_name, salary, vacancy_title, vacancy_description, respond_url]))

vacancy.append(dictionary)
vacancy.append(dictionary_2)
print(vacancy)
vacancy.