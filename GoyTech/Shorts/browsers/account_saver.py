from playwright.sync_api import sync_playwright
import time, json

youtube_accounts = {
    "discountwb1": {"login": "discountwb1@gmail.com", "password": "8l3Vzw0Jt0"},
    "bestsaleswb": {"login": "bestsaleswb@gmail.com", "password": "teeSEu0jnt"},
    "supersaverwb": {"login": "supersaverwb@gmail.com", "password": "UgCxQovJQP"},
}


def youtube(account, name, state, new_acc=False):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        context = browser.new_context(
            storage_state=state, color_scheme="dark", locale="en"
        )
        page = context.new_page()
        page.goto("https://studio.youtube.com", wait_until="domcontentloaded")
        # page.pause()
        if new_acc:
            page.get_by_label("Name").fill(name)
            page.get_by_label("Handle").fill(account)
            page.get_by_label("Create channel").click()
            page.get_by_role("button", name="Continue").click()
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
        time.sleep(3)
        storage_state = context.storage_state()
    return storage_state


if __name__ == "__main__":
    for account_name in youtube_accounts:
        login = youtube_accounts[account_name]["login"]
        passwd = youtube_accounts[account_name]["password"]
        storage_state = google(login, passwd)
        youtube(
            account=account_name,
            name="Супер Скидки ВБ",
            state=storage_state,
            new_acc=False,
        )
        
        

# editknipper@gmail.com:nxu680273xc bestwbssaless Скидки вайлдберриз - V
# nikolzvirgil@gmail.com:swt7nl3skkfx4 Экономия С Вайлдберриз WbSuperSaver -V
# amarillaalbero@gmail.com:pd2gyydfwu wbdiscount Супер Скидки ВБ
# tomskiannabella@gmail.com:7p9g3hdkh94 ВБ Эксклюзивные скидки wbdisscount - XXXX

# huntsenan01@gmail.com:0x1g5a44wij turk_ru_film - X
# lainavigoren@gmail.com:vq1551r19nt ru_turk_films

# ВБ Эксклюзивные скидки
# Экономия С Вайлдберриз
# Мега Скидки ВБ
# Скидки 365 ВБ
# ВБ Халява
# Горячие Предложения ВБ

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

# Берриз Бонусы
# Вайлд Выгода
# ВБ Супер Цены
# Скидочный Рай ВБ
# Вайлд Оферты
# Берриз Сэйвингс
# Супер Скидки Вайлд
# Вайлдберриз Хиты
# Берриз Дилы
# ВБ ПромоКоды
# Вайлд Сейлс
# Берриз Баргин
# Вайлдберриз Гид
# Берриз Бест Цены
