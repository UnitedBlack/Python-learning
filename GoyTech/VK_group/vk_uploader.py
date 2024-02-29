from playwright.sync_api import sync_playwright
import time, json


def upload_vk_clips(
    description_text: str = "Скидки вб",
    vk_url: str = "https://vk.com/ozonwbdiscount",
    input_file: str = "output1.mp4",
):
    with open("Sources/vk_browser.json", "r", encoding="utf-8") as f:
        state = json.loads(f.read())
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=state, color_scheme="dark")
        page = context.new_page()

        page.goto(vk_url, wait_until="domcontentloaded")
        # page.wait_for_selector(('//span[text() = "Клипы"]')).click() 
        page.wait_for_selector('//span[text() = "Опубликовать клип"]').click()
        page.wait_for_selector('//span[text() = "Выбрать файл"]')
        select_file = page.query_selector('//input[@class="file flat_button_file"]')
        select_file.set_input_files(input_file)
        page.wait_for_selector('//textarea[@placeholder="Опишите клип"]').fill(
            description_text
        )
        # mb time sleep
        page.wait_for_selector(
            '//button[@class="FlatButton FlatButton--primary FlatButton--size-m js-video_upload__ready_button"]',
            timeout=900000,
        )
        page.click(
            '//button[@class="FlatButton FlatButton--primary FlatButton--size-m js-video_upload__ready_button"]'
        )
        time.sleep(2)


if __name__ == "__main__":
    upload_vk_clips()
