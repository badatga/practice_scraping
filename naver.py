import requests
from bs4 import BeautifulSoup

url = "https://naver.com"
searchUrl = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=날씨"

#GET 요청 : 
req = requests.get(searchUrl)
html = req.text

# HTML 파싱
soup = BeautifulSoup(html, "html.parser")
# 찾아올 class 지정 - 네이버의 경우 검색결과를 .view_wrap 으로 감싸고 있음
result = soup.select(".view_wrap")

for i in result:
  title = i.select_one(".title_link")
  print(f'title : {title}')
  titleText = i.select_one(".title_link").text
  print(f'title text : {titleText}')
# print(html)

