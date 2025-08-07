from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#class, id 를 css_selector를 이용해서 컨트롤하기 위한 패키지
from selenium.webdriver.common.by import By
# 키보드 입력
from selenium.webdriver.common.keys import Keys

import mysql.connector
import time

keyword = input("검색어 입력 : ")

url = "https://kream.co.kr"

#selenium option
option_ = Options()
option_.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option_)
driver.get(url)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(keyword)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

for i in range(20):
  driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
  time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".item_inner")
product_list = []

for item in items:
  product_name = item.select_one(".translated_name").text

  if '후드' in product_name:
    category = "상의"
    brand = item.select_one('.brand-name').text
    price = item.select_one('.amount').text
    product_info = [category, brand, product_name, price]
    product_list.append(product_info)

connection = mysql.connector.connect(
  host = '127.0.0.1',
  user = 'root',
  passwd = '',
  db = 'KREAM',
  charset = 'utf8mb4'
)

def execute_query(connetion, query, args=None):
  with connection.cursor() as cursor:
    cursor.execute(query, args or ())
    if query.strip().upper().startswith('SELECT'):
      return cursor.fetchall()
    else:
      connection.commit()

driver.quit()

