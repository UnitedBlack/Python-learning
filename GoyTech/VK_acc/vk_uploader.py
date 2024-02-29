from playwright.sync_api import sync_playwright
import time, json


def upload_vk_clips(
    description_text: str,
    vk_url: str,
    input_file: str,
    vc_acc: str,
):
    with open(vc_acc, "r", encoding="utf-8") as f:
        state = json.loads(f.read())
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=state, color_scheme="dark")
        page = context.new_page()

        page.goto(vk_url, wait_until="domcontentloaded")
        page.wait_for_selector('//span[text() = "Опубликовать"]').click()
        page.wait_for_selector('//span[text() = "Выбрать файл"]')
        select_file = page.query_selector('//input[@class="file flat_button_file"]')
        select_file.set_input_files(input_file)
        page.wait_for_selector('//textarea[@placeholder="Опишите клип"]').fill(
            description_text
        )
        page.wait_for_selector(
            '//button[@class="FlatButton FlatButton--primary FlatButton--size-m js-video_upload__ready_button"]',
            timeout=900000,
        )
        page.click(
            '//button[@class="FlatButton FlatButton--primary FlatButton--size-m js-video_upload__ready_button"]'
        )
        time.sleep(2)


if __name__ == "__main__":
    upload_vk_clips(
        description_text="abc",
        vk_url="https://vk.com/clips",
        input_file="editor/temp/input.mp4",
    )
