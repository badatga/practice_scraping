import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36" }
url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)

# 200 -> 정상적인 요청에 대한 응답
# 406 -> 서버가 수용할 수 없다 

html = req.text
soup = BeautifulSoup(html, 'html.parser')

# 사이트 분석 후 list 형태의 데이터 가져오기 
# 관리자 콘솔을 통해 엘리먼트 분석
# lst50 = soup.select(".lst50")
# lst100 = soup.select(".lst100")
# all_lst = lst50 + lst100

# 동일한 문법
all_lst = soup.select(".lst50, .lst100")

chart = []

print('GPT CODE START')
for r in all_lst:
    # 곡 제목
    title = r.select_one(".ellipsis.rank01 a").get_text(strip=True)

    # 가수(여러 명이면 콤마로 이어 붙임)
    singers = ", ".join(a.get_text(strip=True) 
                        for a in r.select(".ellipsis.rank02 a"))

    # 앨범명
    album = r.select_one(".ellipsis.rank03 a").get_text(strip=True)

    chart.append({"title": title, "singer": singers, "album": album})

# 확인
for item in chart:
    print(item)



## 수업용 코드
# for rank, i in enumerate(all_lst, 1):
    