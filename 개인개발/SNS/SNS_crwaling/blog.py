import time
from selenium import webdriver
import pandas as pd


id = "studiohollin@naver.com"
pw = "ghffls2020!"


url_lst = ['https://blog.naver.com/PostList.naver?blogId=studiohollin&categoryNo=0&from=postList']


driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(3)



sns_name=[]
like_lst=[]
comment_lst = []
exposure_lst = []
reach_lst=[]
date_lst = []



for i in range(len(url_lst)):
    url = url_lst[i]
    driver.get(url)
    time.sleep(5)

    like = driver.find_element("xpath",'/html/body/div[6]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[6]/div[1]/div/table[2]/tbody/tr/td[2]/div[3]/div[1]/div[1]/a/div/span/em[2]').text
    comment = driver.find_element("xpath",'/html/body/div[6]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[6]/div[1]/div/table[2]/tbody/tr/td[2]/div[3]/div[1]/div[2]/a/em[1]').text
    date = driver.find_element("xpath",'/html/body/div[6]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[6]/div[1]/div/table[2]/tbody/tr/td[2]/div[1]/div/div[1]/div/div/div[3]/span[2]').text

    sns_name.append('블로그')
    like_lst.append(like)
    comment_lst.append(comment)
    exposure_lst.append('-')
    reach_lst.append('-')
    date_lst.append(date)



blog_record = pd.DataFrame({'활동영역':sns_name,
                            '노출': exposure_lst,
                                    '도달': reach_lst,
                                    '공감': like_lst,
                                    '댓글': comment_lst,
                            '게시일':date_lst})

blog_record.to_csv('C:/Users/USER/Desktop/blog.csv',encoding='cp949')


