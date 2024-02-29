# # for a in href_button_next:
# #     for i in vacancy_link:
# #         CYCLE_INDEX += 1
# #         try:
# #             href = i.get_attribute("href")
# #             try:
# #                 text = i.text
# #             except NoSuchElementException:
# #                 text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']")))
# #             except NoSuchElementException:
# #                 text = "Element not found"
# #             except StaleElementReferenceException:
# #                 text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']")))
# #             except StaleElementReferenceException:
# #                 text = "Element not found"
# #         except StaleElementReferenceException:
# #             href = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']")))
# #         except StaleElementReferenceException:
# #             href = "Element not found"
# #         except NoSuchElementException:
# #             href = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']")))
# #         except NoSuchElementException:
# #             href = "Element not found"
# #         print(f"{CYCLE_INDEX}. Вакансия: {text}, ссылка: {href}")
# #     actions.move_to_element(next_page).click(next_page).perform()


# for a in href_button_next:
#     vacancy_link = driver.find_elements(By.XPATH, "//a[@class='serp-item__title']")
#     for i in vacancy_link:
#         CYCLE_INDEX += 1
#         try:
#             href = i.get_attribute("href")
#             try:
#                 text = i.text
#             except (NoSuchElementException, StaleElementReferenceException):
#                 text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']"))).text
#         except (NoSuchElementException, StaleElementReferenceException):
#             href = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']"))).get_attribute("href")
#         print(f"{CYCLE_INDEX}. Вакансия: {text}, ссылка: {href}")
#     actions.move_to_element(next_page).click(next_page).perform()
#     WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))


# def page_parser():
#     global CYCLE_INDEX
#     for cycle in next_page_button:
#         vacancy_find = driver.find_elements(By.XPATH, "//a[@class='serp-item__title']")
#         for vacancy_link in vacancy_find:
#             CYCLE_INDEX += 1
#             vacancy_url = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']"))).get_attribute("href")
#             vacancy_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='serp-item__title']"))).text
#             actions.move_to_element(next_page).click(next_page).perform()
#             print(CYCLE_INDEX, vacancy_title, vacancy_url)


# page_parser()
import time
from datetime import datetime
print(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
