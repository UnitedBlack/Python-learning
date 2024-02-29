from playwright.sync_api import sync_playwright
import time, json


def tiktok(account, state="", new_acc=False):
    with sync_playwright() as p:
        browser = p.firefox.launch(
            headless=False,
            proxy={
                "server": "http://45.128.58.10:64372",
                "username": "4QAnYVZM",
                "password": "Pj32hj7n",
            },
        )
        with open(f"{account}_browser.json", "r", encoding="utf-8") as file:
            storage_state_file = json.loads(file.read())
        context = browser.new_context(
            storage_state=storage_state_file, color_scheme="dark", locale="en"
        )
        page = context.new_page()
        page.goto("https://www.tiktok.com/")
        page.pause()
        page.wait_for_selector('//button[@id="header-login-button"]').click()
        with page.expect_popup() as page1_info:
            page.get_by_role("link", name="Continue with Google").click()
        page1 = page1_info.value
        time.sleep(2)
        page1.wait_for_selector('//div[@data-item-index="0"]').click()
        time.sleep(25)
        if new_acc:
            page.get_by_text("Month").click()
            page.get_by_role("option", name="March").click()
            page.get_by_text("Day", exact=True).click()
            page.get_by_role("option", name="5", exact=True).click()
            page.get_by_text("Year").click()
            page.get_by_role("option", name="1997").click()
            page.get_by_role("button", name="Next").click()
            page.get_by_placeholder("Username").fill(account)
            page.get_by_role("button", name="Sign up").click()
            time.sleep(10)
        storage_state = context.storage_state()
        with open(f"{account}_browser.json", "w") as f:
            f.write(json.dumps(storage_state))


def google(mail, password):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(color_scheme="dark")
        page = context.new_page()
        page.goto("https://www.google.com/")
        page.wait_for_selector('//a[@aria-label="Войти"]').click()
        page.wait_for_selector('//input[@id="identifierId"]').fill(mail)
        page.click('//span[text()="Далее"]')
        page.wait_for_selector('//input[@type="password"]').fill(password)
        page.click('//span[text()="Далее"]')
        page.pause()
        storage_state = context.storage_state()
    return storage_state


if __name__ == "__main__":
    # storage_state = google(mail="huntsenan01@gmail.com", password="0x1g5a44wij")
    # tiktok(account="wbdisscount")
    tiktok(account="WbSuperSaver")
# editknipper@gmail.com:nxu680273xc bestwbssaless
# tomskiannabella@gmail.com:7p9g3hdkh94 wbdisscount
# nikolzvirgil@gmail.com:swt7nl3skkfx4 WbSuperSaver

# amarillaalbero@gmail.com:pd2gyydfwu turk_seriali
# huntsenan01@gmail.com:0x1g5a44wij turk_ru_film - X
# lainavigoren@gmail.com:vq1551r19nt ru_turk_films

# WbSavingsHub
# EliteWbOffers
# PrimeWbSavings
# WbDealSpotter
# WbSuperSaver
# WbValuePicks
# WbPromoZone
# WbSaleSpotlight


# with open(f"browsers/{account}_browser.json", "r") as f:
#     state = json.loads(f.read())
