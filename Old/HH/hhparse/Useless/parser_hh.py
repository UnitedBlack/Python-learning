from bs4 import BeautifulSoup
import requests
# from forhttp import cookies, headers, params

# vacancy = []

# for_searching = "Маркетолог"
# text_string = params['text'] = for_searching

import requests

cookies = {
    '__ddg1_': 't5FTm9CfSpDBywlhU0hM',
    '_xsrf': '9efde00548c86a99877aaea44fde9602',
    'hhrole': 'anonymous',
    'regions': '1',
    'hhtoken': '5ffHgum3L8qFm2Hwv2jgyNvzxQSo',
    'hhuid': 'rBCqmb8Uy2wWP2T7elo3Rw--',
    'crypted_hhuid': 'FD3DB256DF2C4065FB7876046AD4777A5E6E036185406A78B8692D76CDDB263C',
    'iap.uid': 'dfc32750009143d28f264be9d61841fc',
    '__zzatgib-w-hh': 'MDA0dBA=Fz2+aQ==',
    'redirect_host': 'hh.ru',
    'region_clarified': 'hh.ru',
    'display': 'desktop',
    'GMT': '3',
    'total_searches': '11',
    'device_magritte_breakpoint': 'l',
    'device_breakpoint': 'm',
    'gssc58': '',
    'cfidsgib-w-hh': 'VlcfLnY/o+YRC1bLQZJXh2ditnbRhM8ARrgMdimVcNnLePJcJ0qTJo2kasK4OJYabFl8vuQi79GvoGoVgRrPVxN0YhdsyT9tFoPNO7BHKWwmQV1+DslfULqXwKcEL/uQCUrw7nMNgDBaSeO0RKGVRiVNmJ9jzhl5HS7VCg==',
    'cfidsgib-w-hh': 'VlcfLnY/o+YRC1bLQZJXh2ditnbRhM8ARrgMdimVcNnLePJcJ0qTJo2kasK4OJYabFl8vuQi79GvoGoVgRrPVxN0YhdsyT9tFoPNO7BHKWwmQV1+DslfULqXwKcEL/uQCUrw7nMNgDBaSeO0RKGVRiVNmJ9jzhl5HS7VCg==',
    'gsscgib-w-hh': 'FjvrS5VKsRRKiAla8OinhFnSw3GQdQ2T7p7YbT7/0CRH034/SlwhxLG+D4B6um/RITQoZoWQHIhTm4N+ZiJv4B+PjlXjtQIYqvH1B/AiQJOcNhHMHTVsYN0id/27hVtwq9WMP4k0s5W/K7b9Jv2khJEQlU2BnrrwQZRltM+3u1WVBAWp7JZBbyzJj9sYxQRna/tLhl07zvTYgba6dzpv2aoQohv2Yaar+19joGu24Vlzb+iyeXjQ3Ke8D9IPCA==',
    'fgsscgib-w-hh': 'fSmx37fbc1ce6394fc892387cae95834de9c2d90',
}

headers = {
    'authority': 'hh.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': '__ddg1_=t5FTm9CfSpDBywlhU0hM; _xsrf=9efde00548c86a99877aaea44fde9602; hhrole=anonymous; regions=1; hhtoken=5ffHgum3L8qFm2Hwv2jgyNvzxQSo; hhuid=rBCqmb8Uy2wWP2T7elo3Rw--; crypted_hhuid=FD3DB256DF2C4065FB7876046AD4777A5E6E036185406A78B8692D76CDDB263C; iap.uid=dfc32750009143d28f264be9d61841fc; __zzatgib-w-hh=MDA0dBA=Fz2+aQ==; redirect_host=hh.ru; region_clarified=hh.ru; display=desktop; GMT=3; total_searches=11; device_magritte_breakpoint=l; device_breakpoint=m; gssc58=; cfidsgib-w-hh=VlcfLnY/o+YRC1bLQZJXh2ditnbRhM8ARrgMdimVcNnLePJcJ0qTJo2kasK4OJYabFl8vuQi79GvoGoVgRrPVxN0YhdsyT9tFoPNO7BHKWwmQV1+DslfULqXwKcEL/uQCUrw7nMNgDBaSeO0RKGVRiVNmJ9jzhl5HS7VCg==; cfidsgib-w-hh=VlcfLnY/o+YRC1bLQZJXh2ditnbRhM8ARrgMdimVcNnLePJcJ0qTJo2kasK4OJYabFl8vuQi79GvoGoVgRrPVxN0YhdsyT9tFoPNO7BHKWwmQV1+DslfULqXwKcEL/uQCUrw7nMNgDBaSeO0RKGVRiVNmJ9jzhl5HS7VCg==; gsscgib-w-hh=FjvrS5VKsRRKiAla8OinhFnSw3GQdQ2T7p7YbT7/0CRH034/SlwhxLG+D4B6um/RITQoZoWQHIhTm4N+ZiJv4B+PjlXjtQIYqvH1B/AiQJOcNhHMHTVsYN0id/27hVtwq9WMP4k0s5W/K7b9Jv2khJEQlU2BnrrwQZRltM+3u1WVBAWp7JZBbyzJj9sYxQRna/tLhl07zvTYgba6dzpv2aoQohv2Yaar+19joGu24Vlzb+iyeXjQ3Ke8D9IPCA==; fgsscgib-w-hh=fSmx37fbc1ce6394fc892387cae95834de9c2d90',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

params = {
    'area': [
        '1',
        '1',
    ],
    'employment': [
        'full',
        'part',
        'probation',
    ],
    'excluded_text': '%D0%BC%D0%B0%D1%80%D0%BA%D0%B5%D1%82%D0%BF%D0%BB%D0%B5%D0%B9%D1%81%D1%8B %D0%B2%D0%B0%D0%B9%D0%BB%D0%B4%D0%B1%D0%B5%D1%80%D0%B8%D1%81 %D0%BE%D0%B7%D0%BE%D0%BD %D0%BD%D0%B5%D0%B4%D0%B2%D0%B8%D0%B6%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C %D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0',
    'experience': 'noExperience',
    'industry': [
        '7.541',
        '7.539',
        '11.459',
        '44.393',
    ],
    'professional_role': [
        '170',
        '2',
        '3',
        '37',
        '163',
        '68',
    ],
    'schedule': [
        'fullDay',
        'shift',
        'flexible',
    ],
    'search_field': [
        'name',
        'company_name',
        'description',
    ],
    'clusters': 'true',
    'enable_snippets': 'true',
    'no_magic': 'true',
    'ored_clusters': [
        'true',
        'true',
    ],
    'order_by': 'salary_asc',
    'page': '0',
    'text': '',
    'salary': '',
}

response = requests.get('https://hh.ru/search/vacancy', params=params, cookies=cookies, headers=headers)



def download_pages(start_url):
    url = start_url
    while url is not None:
        response = requests.get(url, cookies=cookies, headers=headers, params=params)
        soup = BeautifulSoup(response.text, 'html.parser')
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        next_link = soup.find("a", {"class": "bloko-button", "rel": "nofollow", "data-qa": "pager-next"})
        url = next_link['href'] if next_link else None
        print(url)

start_url = 'https://hh.ru/search/vacancy?area=1&area=1&employment=full&employment=part&employment=probation&excluded_text=%25D0%25BC%25D0%25B0%25D1%2580%25D0%25BA%25D0%25B5%25D1%2582%25D0%25BF%25D0%25BB%25D0%25B5%25D0%25B9%25D1%2581%25D1%258B+%25D0%25B2%25D0%25B0%25D0%25B9%25D0%25BB%25D0%25B4%25D0%25B1%25D0%25B5%25D1%2580%25D0%25B8%25D1%2581+%25D0%25BE%25D0%25B7%25D0%25BE%25D0%25BD+%25D0%25BD%25D0%25B5%25D0%25B4%25D0%25B2%25D0%25B8%25D0%25B6%25D0%25B8%25D0%25BC%25D0%25BE%25D1%2581%25D1%2582%25D1%258C+%25D1%2581%25D1%2582%25D1%2580%25D0%25BE%25D0%25B9%25D0%25BA%25D0%25B0&experience=noExperience&industry=7.541&industry=7.539&industry=11.459&industry=44.393&professional_role=170&professional_role=2&professional_role=3&professional_role=37&professional_role=163&professional_role=68&schedule=fullDay&schedule=shift&schedule=flexible&search_field=name&search_field=company_name&search_field=description&clusters=true&enable_snippets=true&no_magic=true&ored_clusters=true&ored_clusters=true&order_by=salary_asc&page=0&text=&salary='
download_pages(start_url)



# with open("index1.html", encoding="utf-8") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "lxml")
# xml_doc = src
# all_vacancies_hrefs = soup.find_all(class_="serp-item__title")
# # all_vacancies_hrefs = soup.select(".serp-item__title")
# # all_vacancies_hrefs = soup.find(class_="serp-item").find("span").find_all("a")

# # all_vacancies_hrefs = soup.find_all('h3')

# # print(all_vacancies_hrefs)
# print(len(all_vacancies_hrefs))

# for i, item in enumerate(all_vacancies_hrefs):
#      item_text = item.text
#      item_href = item.get("href")
#      print(f"{i+1}. {item_text}: {item_href}")


