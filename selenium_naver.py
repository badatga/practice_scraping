from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

keyword = input("검색어를 입력해주세요 : ")
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + keyword

option_ = Options() #인스턴스 생성 / 객체화
option_.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option_)
driver.get(url) # request -> 소스코드  / 셀레니움 -> 화면을 가져옵니다. ->why 브라우저에게 명령을 내렸기 때문에
# time.sleep(2)

cnt = 0
# 스크롤 기능 
# while True:
#   driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#   cnt += 1
#   if cnt == 6:
#     print('goodbye')
#     break

# 강의용 코드
for i in range(6):
  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(1)

html = driver.page_source 

soup = BeautifulSoup(html, "html.parser")

result = soup.select(".view_wrap")

for i in result:
    ad = i.select_one(".spblog.ico_ad") #<i class="spblog ico_ad">광고</i>  or None

    if not ad:
        title = i.select_one(".title_link").text #우리가 원하는건 그 안에 텍스트!!!!
        link = i.select_one(".title_link")["href"]
        writer = i.select_one(".name").text
        dsc = i.select_one(".dsc_link").text
        
        print(f'제목 : {title}')
        print(f'링크 : {link}')
        print(f'작성자 : {writer}')
        print(f'글요약 : {dsc}')
        print()
  
driver.quit()