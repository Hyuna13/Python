import time
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

#네이버이동
browser.get("http:/naver.com")

#로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#id.pw입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

#로그인버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

#id 새로입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

#html정보출력
print(browser.page_source)

#브라우저 종료
browser.close()#탭만종료
browser.quit()#전체 브라우저 종료