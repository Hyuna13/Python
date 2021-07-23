import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
res = requests.get(url, headers=headers )
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
#print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:

  #광고제품은 제외
  ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
  if ad_badge:
    print("  <광고상품 제외>  ")
    continue

  #애플제품 제외
  name = item.find("div", attrs={"class":"name"}).get_text()
  if 'Apple' in name:
    print("<애플상품 제외>")
    continue

  price = item.find("strong", attrs={"class":"price-value"}).get_text()

  #리뷰 100이상 평점4.5이상만 조회
  rate = item.find("em", attrs={"class":"rating"})
  if rate:
    rate = rate.get_text()
  else:
    print("<평점 없는 상품 제외>")
    continue

  rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
  if rate_cnt:
    rate_cnt = rate_cnt.get_text()
    rate_cnt = rate_cnt[1:-1]
  else:
    print("<평점 수 없는 상품 제외>")
    continue

  if float(rate) >= 4.5 and int(rate_cnt) >= 100:
      print(name, price, rate, rate_cnt)

  


