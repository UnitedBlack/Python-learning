from playwright.sync_api import sync_playwright
import requests, json

from req_config import proxies, headers


def get_url(stamp="0"):
    url = f"https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1702829206&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%29&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor={stamp}&device_id=7313595501092587040&device_platform=web_pc&focus_state=true&from_page=user&history_len=2&is_fullscreen=false&is_page_visible=true&language=en&os=windows&priority_region=&referer=&region=US&screen_height=720&screen_width=1280&secUid=MS4wLjABAAAAr-kgbLODubBZ7TvoYGk8C5mqibgbBuZPrs57SHjk44LG5AqOk6s2Ch1rA0iMJHcn&tz_name=Europe%2FMoscow&webcast_language=en&msToken=lO7Kr0pqirburiyHcV141c7HAymEJpJraGWf9I739up5VRIf_CoB2krZa9PfVIi7p0f68daZS_9ZE7MB2782fA16puPQJm28SdLROtj6MbwKaCmu3dBTMWtp-ap-cxekqGo=&X-Bogus=DFSzsIVOoNXANChLtuFRHt9WcBJK&_signature=_02B4Z6wo00001Vc051QAAIDBVzTnVvyR3uVXNuPAADC18f"
    return url


def parse_tiktok_video(acc_url):
    # response = requests.get(url=get_url(), headers=headers, proxies=proxies)
    response = requests.get(
        url="https://www.tiktok.com/@_liiviis_/video/7291715423182032129", headers=headers, proxies=proxies
    )
    # print(response.text)
    resp = response.cookies
    print(resp)
    # with open("zalupa.json", "w", encoding="utf-8") as file:
    #     file.write(json.dumps(resp, ensure_ascii=True))
    # for i, aboba in enumerate(resp["itemList"]):
    #     print(i, aboba["id"])

    # with sync_playwright() as p:
    #     browser = p.firefox.launch(
    #         headless=False,
    #         proxy={
    #             "server": "http://45.128.58.10:64372",
    #             "username": "4QAnYVZM",
    #             "password": "Pj32hj7n",
    #         },
    #     )
    #     # with open(f"{account}_browser.json", "r", encoding="utf-8") as file:
    #     #     storage_state_file = json.loads(file.read())
    #     context = browser.new_context(color_scheme="dark", locale="en")
    #     page = context.new_page()
    #     page.goto(acc_url)
    #     page.pause()


if __name__ == "__main__":
    parse_tiktok_video("https://www.tiktok.com/@wildberries_halyva24")
# 1699685228000
# 1692783625000
# 1696482533000
