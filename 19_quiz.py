import requests
from bs4 import BeautifulSoup


url = "https://new.land.naver.com/complexes/111515?ms=37.49751,127.107693,17&a=APT:ABYG:JGC&b=A1&e=RETAIL"
res =requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

#with open("quiz.html", "w", encoding="utf8") as f:
#  f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for index, row in enumerate(data_rows):
    columns = row.find_all("td")

    print("======= 매물 {} =======".format(index+1))
    print("거래 : ", columns[0].get_text().strip())
    print("면적 :", columns[1].get_text().strip(), "(공급/전용)")
    print("가격 :", columns[2].get_text().strip(), "(만원)")
    print("동 :", columns[3].get_text().strip())
    print("층 :", columns[4].get_text().strip())

