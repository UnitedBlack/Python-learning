from playwright.sync_api import sync_playwright
import time, json


def upload_tt(
    account_name: str,
    input_file: str,
    description_text: str = "Скидки на товары в шапке профиля",
):
    print("Uploading tiktok video")
    with open(f"browsers/{account_name}_browser.json", "r", encoding="utf-8") as f:
        state = json.loads(f.read())
    with sync_playwright() as p:
        browser = p.firefox.launch(
            headless=False,
            proxy={
                "server": "http://45.128.58.10:64372",
                "username": "4QAnYVZM",
                "password": "Pj32hj7n",
            },
        )
        context = browser.new_context(
            storage_state=state, color_scheme="dark", locale="en"
        )
        page = context.new_page()
        if account_name in ["turk_seriali"]:
            page.goto("https://www.tiktok.com/upload")
        else:
            page.goto(
                "https://www.tiktok.com/creator-center/upload?from=upload&lang=en",
                wait_until="domcontentloaded",
            )
        page.frame_locator("iframe").get_by_role("button", name="Select file").wait_for(
            state="visible", timeout=120000
        )
        page.frame_locator("iframe").locator(
            "//input[@type='file' and @accept='video/*']"
        ).set_input_files(input_file)
        page.frame_locator("iframe").locator(
            '//div[@class="notranslate public-DraftEditor-content"]'
        ).fill(description_text)
        if account_name in ["turk_seriali"]:
            page.frame_locator("iframe").get_by_role(
                "button", name="Change video"
            ).wait_for(state="visible", timeout=120000)
        else:
            page.frame_locator("iframe").locator('//video[@class="player"]').wait_for(
                state="visible", timeout=120000
            )
        # page.pause()
        page.frame_locator("iframe").get_by_role("button", name="Post").click()
        page.frame_locator("iframe").get_by_text(
            "Your video is being uploaded to TikTok!"
        ).wait_for(state="visible", timeout=120000)
        storage_state = context.storage_state()
        with open(f"browsers/{account_name}_browser.json", "w") as f:
            f.write(json.dumps(storage_state))
        return


if __name__ == "__main__":
    upload_tt(
        account_name="turk_seriali",
        input_file="video/editor/temp/Супер находки вб.mp4",
    )
