import time
from playwright.sync_api import sync_playwright


def respond(url, text=""): 
    
    page.goto(url, wait_until="domcontentloaded")
    try:
        page.wait_for_selector('div[class="vacancy-action vacancy-action_after-body"]', timeout=6000)
        zalupa1 = page.query_selector('div[class="vacancy-action vacancy-action_after-body"]').text_content()
        if zalupa1: print(zalupa1)

    except:
        page.wait_for_selector('//div[@class="vacancy-response-popup-subtitle"][2]/div[@class="bloko-text bloko-text_strong"]', timeout=3000)
        zalupa2 = page.query_selector('//div[@class="vacancy-response-popup-subtitle"][2]/div[@class="bloko-text bloko-text_strong"]').text_content()
        if zalupa2: print(zalupa2)

def login():
    page.goto("https://hh.ru/account/login?backurl=%2F&hhtmFrom=main", wait_until="domcontentloaded")
    page.query_selector('button[data-qa="expand-login-by-password"]').click()
    page.query_selector('input[data-qa="login-input-username"]').fill('79771294588')
    page.query_selector('input[data-qa="login-input-password"]').fill('Bibaboba1!')
    page.query_selector('button[data-qa="account-login-submit"]').click()
    time.sleep(2)
    respond(url="https://hh.ru/applicant/vacancy_response?vacancyId=87199093")


      
with sync_playwright() as playwright: 
    browser = playwright.firefox.launch(headless=False) 
    context = browser.new_context() 
    # context.set_default_navigation_timeout(5)
    page = context.new_page()    
    login()


