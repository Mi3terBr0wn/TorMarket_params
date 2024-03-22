from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import time

from auth_info import login_email
from auth_info import login_password


# настройка веб драйвера селениум
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

url = 'https://v-tormarket.ru/partner'
driver.get(url)

time.sleep(3)

login_field = driver.find_element(By.CSS_SELECTOR, '#main > div > section > div > div > div > div > div > div > div:nth-child(1) > form > div.form-group.email > input')
password_field = driver.find_element(By.CSS_SELECTOR, '#main > div > section > div > div > div > div > div > div > div:nth-child(1) > form > div.form-group.password > input')
button_element = driver.find_element(By.CSS_SELECTOR, '#main > div > section > div > div > div > div > div > div > div:nth-child(1) > form > button')

login_field.send_keys(login_email)
password_field.send_keys(login_password)
time.sleep(3)
button_element.click()
main_url = driver.current_url
time.sleep(3)

driver.fullscreen_window()

my_products_section_url = driver.find_element(By.CSS_SELECTOR, '#main > div > div > div > div > div.col-12.col-lg-3.col-xl-2.left-panel > div > div.menus.mt-5.hide-mobile > div:nth-child(2) > div:nth-child(2) > ul > li:nth-child(3) > a')
my_products_section_url.click()
time.sleep(3)

my_products_section_url = driver.current_url
products_file = open("products_file.txt", 'r')

for product in products_file:
    vendor_code = product
    '''читаем артикул из файла. тестовая заглушка - один артикул'''
    vendor_code_field = driver.find_element(By.NAME, 'sku')
    vendor_code_field.clear()
    vendor_code_field.send_keys(product)
    filter_button = driver.find_element(By.CSS_SELECTOR, '#filterProducts > div > div:nth-child(5) > button')
    filter_button.click()

    edit_product_url = driver.find_element(By.CSS_SELECTOR, '#content > div:nth-child(3) > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div.product-name > a')
    edit_product_url.click()

    attributes_section_url = driver.find_element(By.CSS_SELECTOR, '#content > div.dst-admin-filter.mb-3 > ul > li:nth-child(3) > a')
    attributes_section_url.click()
    attributes_dict = {
        'material': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(2)'), #материал
        'height': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(4)'), #высота
        'width': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(5)'), #ширина
        'depth': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(6)'), #глубина
        'color': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(7)'), #цвет
        'type': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(8)'), #тип
        'purpose': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(9)'), #назначение
        'style': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(10)'), #стиль
        'installation_type': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(11)'), #тип установки
        'number_of_doors': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(12)'), #количество дверей
        'type_of_door_opening': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(13)'), #тип открывания дверей
        'mirror': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(14)'), #зеркало
        'features': driver.find_element(By.CSS_SELECTOR, '#formProduct > div.toolbar.toolbar-top.mb-3 > div > div > select > option:nth-child(15)') #особенности

    }

    for attribute in attributes_dict.values():
        attribute.click()
        #заполнить атрибыты текстом из файла




    driver.back()
    driver.back()




'''
в файле перебираем все строки
делаем поиск по артикулу
открываем на редактирование карточку в новой вкладке
переходим в атрибуты
выбираем по одному атрибуты (цикл, перебираем все доступные атрибуты),  жмем добавить
вводим в поле выберете значения или новое значение + добавить
сохранить
закрыть вкладку

'''

print(main_url)

'''
button_element = driver.find_element(By.CSS_SELECTOR, '#mini-service-box > div:nth-child(2) > div > div:nth-child(2) > div')
button_element.click()
time.sleep(5)

new_2_url = driver.current_url

page_source = driver.page_source
driver.quit()
soup = BeautifulSoup(page_source, 'html.parser')

with open("games_list.txt", "a", encoding='utf-8') as file:
    file.write(soup.text)


button_element = driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div/div/div[1]/div/div[5]/a')
button_element.click()
time.sleep(5)

main_url = driver.current_url

page_source = driver.page_source
driver.quit()
soup = BeautifulSoup(page_source, 'html.parser')

with open("games_list.txt", "a", encoding='utf-8') as file:
    file.write(soup.text)
'''