from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()

#페이지이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

#지정한 위치로 스크롤내리기
#모니터(해상도) 높이 1080 위치로 스크롤 내리기
#browser.execute_script("window.scrollTo(0, 1080)")

#화면 가장아래로 스크롤내리기
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 #2초에 한번씩 스크롤 내림

#현재 문서높이 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복수행
while True:
  #스크롤 가장 아래로 내림
  browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  
  #페이지 로딩 대기
  time.sleep(interval)

  #현재 문서 높이 가져와서 저장
  curr_height = browser.execute_script("return document.body.scrollHeight")
  if curr_height == prev_height:
    break

  prev_height = curr_height
print("DONE")


import requests
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, "lxml")

#movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    #할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print("할인되지 않은 영화는 제외")
        continue
    #할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    #링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른링크 : https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 : {original_price}")
    print(f"할인 후 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)

browser.quit()

