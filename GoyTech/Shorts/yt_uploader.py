from playwright.sync_api import sync_playwright
import time, json


def upload_yt(
    account_name: str,
    input_file: str = "",
    title: str = "Вб скидки",
    description_text: str = "Артикулы на товары в шапке профиля",
):
    print("Uploading youtube shorts")
    with open(f"browsers/{account_name}_browser.json", "r", encoding="utf-8") as f:
        state = json.loads(f.read())
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(
            storage_state=state, color_scheme="dark", locale="en"
        )
        page = context.new_page()
        page.goto("https://studio.youtube.com", wait_until="domcontentloaded")
        page.get_by_label("Upload videos").click()
        page.query_selector('//input[@type="file"]').set_input_files(input_file)
        if account_name in ["bestwbssaless", "wbdiscount"]:
            page.wait_for_selector(
                '//div[@aria-label="Tell viewers about your video (type @ to mention a channel)"]'
            ).fill(description_text)
            page.wait_for_selector(
                '//tp-yt-paper-radio-button[@name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]'
            ).click()
            page.wait_for_selector(
                selector='//ytcp-button[@id="next-button"]', state="visible"
            ).click()
            page.wait_for_selector(
                selector='//ytcp-button[@id="next-button"]', state="visible"
            ).click()
            page.wait_for_selector(
                selector='//ytcp-button[@id="next-button"]', state="visible"
            ).click()
            page.wait_for_selector('//tp-yt-paper-radio-button[@name="PUBLIC"]').click()
            page.wait_for_selector('//ytcp-button[@id="done-button"]').click()
        elif account_name in ["WbSuperSaver"]:
            page.get_by_label(
                "Tell viewers about your video (type @ to mention a channel)"
            ).fill(description_text)
            page.get_by_role("radio", name="No, it's not made for kids").click()
            page.locator("ytcp-uploads-dialog").get_by_role(
                "button", name="Next"
            ).click()
            page.locator("ytcp-uploads-dialog").get_by_role(
                "button", name="Next"
            ).click()
            page.locator("ytcp-uploads-dialog").get_by_role(
                "button", name="Next"
            ).click()
            page.get_by_role("radio", name="Public").click()
            page.get_by_role("button", name="Publish").click()

        try:
            page.get_by_role("heading", name="Video processing").wait_for(
                state="visible"
            )
        except Exception:
            page.get_by_role("heading", name="Video published").wait_for(
                state="visible"
            )
        time.sleep(3)
        storage_state = context.storage_state()
        with open(f"browsers/{account_name}_browser.json", "w") as f:
            f.write(json.dumps(storage_state))


if __name__ == "__main__":
    upload_yt(
        account_name="wbdiscount",
        input_file="video/editor/temp/top.wildber.mp4",
    )
