from playwright.sync_api import sync_playwright
import time, json

yt_upload_link = "https://studio.youtube.com/channel/UC_aZ2REyM_6zHEUmOv2f4hw/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"

def upload_yt_clips(
    yt_url: str = "https://youtube.com",
):
    with sync_playwright() as p:
        with open("Sources/yt_browser.json", "r", encoding="utf-8") as f:
            state = json.loads(f.read())
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=state, color_scheme="dark")
        page = context.new_page()
        page.goto(yt_url)
        time.sleep(15)


upload_yt_clips(
    yt_url=yt_upload_link
)
# wildozon1@gmail.com
