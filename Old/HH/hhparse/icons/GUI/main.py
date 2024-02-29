import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

time = datetime.now().strftime("%H-%M")
CYCLE_INDEX = 0
options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
driver.set_script_timeout(5)
actions = ActionChains(driver)
new_var = "asdffasdasdf"
print("Loading page...")
driver.get(f"https://hh.ru/search/vacancy?area=1&search_field=name&search_field=company_name&search_field=description&enable_snippets=true&L_save_area=true&text=python&salary=450000&only_with_salary=true")

try:
    next_page = driver.find_element(By.XPATH, "//a[@data-qa='pager-next']")
    next_page_button = next_page.get_attribute("href")
except (NoSuchElementException, StaleElementReferenceException):
    next_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
        By.XPATH, "//a[@data-qa='pager-next']"))).get_attribute("href")


def page_parser():
    global CYCLE_INDEX
    for cycle in next_page_button:
        vacancy_find_xpath = driver.find_elements(
            By.XPATH, "//a[@class='serp-item__title']")
        for vacancy_find in vacancy_find_xpath:
            CYCLE_INDEX += 1
            try:
                vacancy_link = vacancy_find.get_attribute("href")
                try:
                    vacancy_title = vacancy_find.text
                except (NoSuchElementException, StaleElementReferenceException):
                    vacancy_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                        By.XPATH, "//a[@class='serp-item__title']"))).text
            except (NoSuchElementException, StaleElementReferenceException):
                vacancy_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
                    By.XPATH, "//a[@class='serp-item__title']"))).get_attribute("href")
            try:
                vacancy_link_clean = re.sub('vologda\.', '', vacancy_link)
            except:
                vacancy_link_clean = vacancy_link
            output = (f"{vacancy_title}, {vacancy_link_clean}")
            with open(f'Parsed-{time}.txt', 'a', encoding='utf-8') as file: file.write(output + "\n")
        actions.move_to_element(next_page).click(next_page).perform()
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    return



if __name__ == "__main__":
    page_parser()
    driver.quit()

