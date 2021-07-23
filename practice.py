import re
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

def create_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(index, title, link):
        print("{}. {}".format(index+1, title))
        print("  링크 : {}".format(link))
    

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9A%A9%EC%9D%B8+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&tqi=hMjmGwp0J1ZssDAia%2Fssssssto8-208477"
    soup = create_soup(url)
    #날씨
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    #온도
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨", "")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()
    #강수량
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip() 
    #미세먼지
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text()#미세먼지
    pm25 = dust.find_all("dd")[1].get_text()#초미세먼지
    #출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))  
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()
    
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url ="https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("  (링크 : {})".format(link))
    print()

def scrape_IT_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    IT_news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for index, news in enumerate(IT_news_list):
        a_idx = 0
        img = news.find("img")
        if img:
          a_idx = 1
        
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print()
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
    

if __name__ == "__main__":
    scrape_weather() #오늘 날씨정보가져오기
    scrape_headline_news() #헤드라인 뉴스 가져오기
    scrape_IT_news() #IT 뉴스 가져오기
    scrape_english() # 오늘의 영어회화 가져오기