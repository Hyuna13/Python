from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2880×1800")
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()