import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

for i in range(1, 6):
  #print("페이지:", i)
  url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)

  res = requests.get(url, headers=headers)
  res.raise_for_status()
  soup = BeautifulSoup(res.text,"lxml")

  items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

  for item in items:

    #광고제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
      #print("  <광고상품 제외>  ")
      continue

    #애플제품 제외
    name = item.find("div", attrs={"class":"name"}).get_text()
    if 'Apple' in name:
      #print("<애플상품 제외>")
      continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text()

    #리뷰 100이상 평점4.5이상만 조회
    rate = item.find("em", attrs={"class":"rating"})
    if rate:
      rate = rate.get_text()
    else:
      #print("<평점 없는 상품 제외>")
      continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
    if rate_cnt:
      rate_cnt = rate_cnt.get_text()
      rate_cnt = rate_cnt[1:-1]
    else:
      #print("<평점 수 없는 상품 제외>")
      continue

    link = item.find("a", attrs={"class":"search-product-link"})["href"]

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
         #print(name, price, rate, rate_cnt)
         print(f"제품명 : {name}")
         print(f"가격 : {price}")
         print(f"평점 : {rate}점 ({rate_cnt}개)")
         print("바로가기 : {}".format("https://www.coupang.com"+link))
         print("-"*100) #줄긋기

