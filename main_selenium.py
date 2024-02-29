from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import requests
import time

from auth_info import login_email
from auth_info import login_password

# настройка веб драйвера селениум
options = webdriver.ChromeOptions()
options.add_argument("--headless")
# Run Chrome in headless mode
driver = webdriver.Chrome(options=options)

url = 'https://v-tormarket.ru/auth/login'
driver.get(url)

login_field = driver.find_element(By.CSS_SELECTOR, '#main > div > div > div > div.products.help-center > div > div > div > div.col-12.col-md-4.order-sm-first.order-xs-first.order-md-last.mb-3 > div:nth-child(1) > div > form > div.form-group.email > input')
password_field = driver.find_element(By.CSS_SELECTOR, '#main > div > div > div > div.products.help-center > div > div > div > div.col-12.col-md-4.order-sm-first.order-xs-first.order-md-last.mb-3 > div:nth-child(1) > div > form > div.form-group.password > input')
button_element = driver.find_element(By.CSS_SELECTOR, '#main > div > div > div > div.products.help-center > div > div > div > div.col-12.col-md-4.order-sm-first.order-xs-first.order-md-last.mb-3 > div:nth-child(1) > div > form > button')

login_field.send_keys(login_email)
password_field.send_keys(login_password)
button_element.click()
time.sleep(5)

new_url = driver.current_url

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

new_url = driver.current_url

page_source = driver.page_source
driver.quit()
soup = BeautifulSoup(page_source, 'html.parser')

with open("games_list.txt", "a", encoding='utf-8') as file:
    file.write(soup.text)