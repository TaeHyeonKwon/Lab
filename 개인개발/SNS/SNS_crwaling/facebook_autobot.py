import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


path = "chromedriver.exe"
url = "https://www.facebook.com/login/"

id = "studiohollin@naver.com"
pw = "ghffls2020!"

tag_lst=['#메타버스']


# 크롬 옵션 정의 (1이 허용, 2가 차단)
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(path, options=chrome_options)
driver.get(url)




# 로그인
# driver.find_element("xpath", '/html/body/div/div[1]/div[2]/div/div[2]/div/div/div/div[2]/div/div').click()
driver.find_element("name", 'email').send_keys(id)
driver.find_element("name", 'pass').send_keys(pw)
driver.find_element("id", 'loginbutton').click()


time.sleep(5)

# 태그검색

blank = driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input')
blank.click()
time.sleep(random.randint(2,5))


input_blank = driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input')
message = random.choice(tag_lst)
input_blank.send_keys(message)
time.sleep(random.randint(2,5))

input_blank.send_keys(Keys.RETURN)

# 좋아요 클릭 (좋아요 버튼 접근이 안됌)

time.sleep(8)


for i in range(1,4):
    like = driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/div[4]/div/div/div/div/div/div/div[{}]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div/div/div[2]/div/div[1]/div[1]'.format(i))
    time.sleep(random.randint(1,3))
    like.click()

