import requests
from bs4 import BeautifulSoup
from auth_info import login_email
from auth_info import login_password

user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
url = 'https://v-tormarket.ru/partner'

session = requests.Session()
r = session.get(url)
print(r)

session.headers.update()
session.headers.update({'Referer': url})
session.headers.update({'User-Agent': user_agent_val})

soup = BeautifulSoup(r.text, features="lxml")
csrf_token = soup.find(attrs={'name':'csrf_token'})['value']

data = {
    'csrf_token': csrf_token,
    'login_email': login_email,
    'login_password': login_password,
    'remember': '1'
}

session.headers.update()
session.headers.update({'Referer': url})
session.headers.update({'User-Agent': user_agent_val})
responce = session.post(url, data=data, cookies=session.cookies)
print(responce)

url_edit_1 = 'https://v-tormarket.ru/partner/11378/home'
session.headers.update()
session.headers.update({'Referer': 'https://v-tormarket.ru/partner'})
session.headers.update({'User-Agent': user_agent_val})

responce_edit_1 = session.get(url_edit_1, cookies=session.cookies)
print(responce_edit_1)

with open("url_success.html", "w", encoding="utf-8") as f:
    f.write(responce_edit_1.text)

'''
page_1_url = 'https://v-tormarket.ru/partner/11378/products?category_id=0&name=0&sku=0&code=0&list=0&count=0&page=1'
page_1_responce = session.get(page_1_url, headers=header).text

print(page_1_responce)

with open("url_success.html", "w", encoding="utf-8") as f:
    f.write(page_1_responce)
'''

'''
url = url_sample
session = requests.Session()
r = session.get(url, headers={
    'User-Agent': user_agent_val
})

session.headers.update({'Referer': url})
session.headers.update({'User-Agent': user_agent_val})

_xsrf = session.cookies.get('_xsrf', domain="v-tormarket.ru")

post_request = session.post(url, {
    'backUrl': 'https://v-tormarket.ru/partner',
    'login_email': login_email,
    'login_password': login_password,
    '_xsrf': _xsrf,
    'remember': 'yes',
})
print(post_request)

with open("hh_success.html", "w", encoding="utf-8") as f:
    f.write(post_request.text)

# создание файла со ссылками на карточки
href_list = open("href_list.txt", 'w')
href_list.close()

for i in range(1, 5):
    str_url = 'https://v-tormarket.ru/partner/11378/products?category_id=0&name=0&sku=0&code=0&list=0&count=0&page=' + str(i)

    print(response)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        product_actions = soup.find('div', class_='dst-product-admin')

        if product_actions:
            links = product_actions.find_all('a')

            for link in links:
                href = link.get('href')
                if '/partner/11378/products/edit/' in href:
                    with open('href_list.txt', 'a') as file:
                            file.write({href} + '\n')
        else:
            print('Не удалось найти блок product-actions на странице.')

    else:
        print('Не удалось загрузить страницу. Код статуса:', response.status_code)
'''
