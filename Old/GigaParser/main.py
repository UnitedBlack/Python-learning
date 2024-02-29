import requests
import json
import csv
from bs4 import BeautifulSoup as bs
from datetime import datetime

cookies = {
    'lang': 'ru',
    '_csrf': '493157b36a270dc54c97831058383f4c2b4fdad55c661a5c43cba1183d2ca33fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Vcq9MqM8qxff574zGNweNSRO5KALDF_Y%22%3B%7D',
    'phonesIdent': '6c0c8cf1b790cdb2fcedb3039b4f0954de19dd550ec2341ea0182702101b91e9a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22e1ae0d35-acbb-4bb7-bd1e-38725edab56a%22%3B%7D',
    'cartUserCookieIdent_v3': '12de532f4c7295ea5a53d8c248f806cb972d17725755d39e8369fd04bf80db5ba%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%220a4dc77b-112d-3cf8-9b04-9910618b26a1%22%3B%7D',
    'city_path': 'moscow',
    'current_path': '605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
    'qrator_ssid': '1693922872.693.acyj7nlTXBJEfJZc-flsjts7q2jc6eposd35cdmb4ku1s5qla',
    '_ab_': '%7B%22search-sandbox%22%3A%22default%22%2C%22catalog-hit-filter%22%3A%22filtr_hit_default%22%7D',
    'PHPSESSID': 'a6177ac6a6e79e79348904c431cf4499',
    'qrator_jsid': '1693922871.809.efCPiVOXwgJeRRcr-1m3i8uen04c9rsfu61gp19hgpoa2jp7o',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'lang=ru; _csrf=493157b36a270dc54c97831058383f4c2b4fdad55c661a5c43cba1183d2ca33fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Vcq9MqM8qxff574zGNweNSRO5KALDF_Y%22%3B%7D; phonesIdent=6c0c8cf1b790cdb2fcedb3039b4f0954de19dd550ec2341ea0182702101b91e9a%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22e1ae0d35-acbb-4bb7-bd1e-38725edab56a%22%3B%7D; cartUserCookieIdent_v3=12de532f4c7295ea5a53d8c248f806cb972d17725755d39e8369fd04bf80db5ba%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%220a4dc77b-112d-3cf8-9b04-9910618b26a1%22%3B%7D; city_path=moscow; current_path=605bfdc517d7e9e23947448a9bf1ce16ac36b884434a3fdb10db053793c50392a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%2230b7c1f3-03fb-11dc-95ee-00151716f9f5%22%2C%22cityName%22%3A%22%5Cu041c%5Cu043e%5Cu0441%5Cu043a%5Cu0432%5Cu0430%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; qrator_ssid=1693922872.693.acyj7nlTXBJEfJZc-flsjts7q2jc6eposd35cdmb4ku1s5qla; _ab_=%7B%22search-sandbox%22%3A%22default%22%2C%22catalog-hit-filter%22%3A%22filtr_hit_default%22%7D; PHPSESSID=a6177ac6a6e79e79348904c431cf4499; qrator_jsid=1693922871.809.efCPiVOXwgJeRRcr-1m3i8uen04c9rsfu61gp19hgpoa2jp7o',
    'Origin': 'https://www.dns-shop.ru',
    'Referer': 'https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/no-referrer',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
    'X-CSRF-Token': 'vsvPQIqCxX-DciyDTkpUbyJpOQS_ayc-0dsuqIYOXvzoqL55x_OIR_IKSuV7fWAVZSdOYfE4dXHkkG_kwkgBpQ==',
    'X-Requested-With': 'XMLHttpRequest',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = 'data={"type":"product-buy","containers":[{"id":"as-LDIJt5","data":{"id":"4853000"}},{"id":"as-bh2BoB","data":{"id":"5074554"}},{"id":"as-K2ImKJ","data":{"id":"5074555"}},{"id":"as-zVuY7n","data":{"id":"5074520"}},{"id":"as-hjYDF9","data":{"id":"4730217"}},{"id":"as-ZZoGzD","data":{"id":"5082268"}},{"id":"as--vSs7V","data":{"id":"5018068"}},{"id":"as-3TRQq3","data":{"id":"5074553"}},{"id":"as-_hfyzQ","data":{"id":"5411942"}},{"id":"as-onqwQ9","data":{"id":"5085263"}},{"id":"as-pHgfLT","data":{"id":"5094947"}},{"id":"as-1nmYF6","data":{"id":"5419328"}},{"id":"as-e4ro5-","data":{"id":"5357383"}},{"id":"as-2AWyZJ","data":{"id":"5414835"}},{"id":"as-Gngass","data":{"id":"4864261"}},{"id":"as-RqMdgO","data":{"id":"4876024"}},{"id":"as-Pvwr06","data":{"id":"5009427"}},{"id":"as-FRmrrP","data":{"id":"4846103"}}]}'

response = requests.post('https://www.dns-shop.ru/ajax-state/product-buy/',
                         cookies=cookies, headers=headers, data=data)

print(response)
