from playwright.sync_api import sync_playwright
import json, time


def parse_tiktok_video(acc_url):
    with sync_playwright() as p:
        browser = p.firefox.launch(
            headless=False,
            proxy={
                "server": "http://45.128.58.10:64372",
                "username": "4QAnYVZM",
                "password": "Pj32hj7n",
            },
        )
        # with open(f"{account}_browser.json", "r", encoding="utf-8") as file:
        #     storage_state_file = json.loads(file.read())
        context = browser.new_context(color_scheme="dark", locale="en")
        page = context.new_page()
        page.goto(acc_url, wait_until="domcontentloaded")
        time.sleep(3)
        page.goto(acc_url, wait_until="domcontentloaded")
        videos = []
        page.wait_for_selector('//div[@data-e2e="user-post-item-list"]')
        for _ in range(20):
            main_block = page.query_selector_all(
                '//div[contains(@class, "DivContainer-StyledDivContainerV2")]//a'
            )
            for video in main_block:
                video_url = video.get_attribute("href")
                if video_url not in videos:
                    videos.append(video_url)
            page.evaluate(
                f"document.querySelector('a[href=\"{main_block[-1].get_attribute('href')}\"]').scrollIntoView()"
            )
        with open(
            f"{acc_url.replace('https://www.tiktok.com/@', '')}.json",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(json.dumps(videos))


if __name__ == "__main__":
    parse_tiktok_video("https://www.tiktok.com/@wildberrhomee")
    parse_tiktok_video("https://www.tiktok.com/@wb_wildberries1")
    parse_tiktok_video("https://www.tiktok.com/@wb_salee")
    # parse_tiktok_video("https://www.tiktok.com/@top.wildber")
# https://www.tiktok.com/@wildberrhomee
# https://www.tiktok.com/@wb_wildberries1
# https://www.tiktok.com/@wb_salee
