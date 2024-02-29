import requests, json

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7",
    "Connection": "keep-alive",
    "Host": "catalog.wb.ru",
    "Origin": "https://www.wildberries.ru",
    "Referer": "https://www.wildberries.ru/catalog/zhenshchinam/odezhda/bluzki-i-rubashki",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
}

url_bluzki_i_rubashki = f"https://catalog.wb.ru/catalog/bl_shirts/catalog?appType=1&cat=8126&curr=rub&dest=-1257786&page=1&sort=popular&spp=30"
# response = requests.get(url_bluzki_i_rubashki, headers=headers)
# print(response.text)
# with open("js.json", "w", encoding="utf-8") as f:
#     f.write(json.dumps(response.json(), ensure_ascii=False))

with open("js.json", "r", encoding="utf-8") as f:
    data = json.loads(f.read())

products = data["data"]["products"]

for product in products:
    print(product["name"])
