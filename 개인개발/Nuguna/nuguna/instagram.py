import random
import time
import pandas as pd
from selenium import webdriver



sns_name=[]
like_lst = []
comment_lst=[]
reach_lst =[]
exposure_lst=[]
date_lst = []



#id = 'studiohollin@naver.com'
#pw = 'ghffls2020!'



instaemail = Element("instaID")
instapw = Element("instaPW")
results = Element("result")



# id = 'kwon1224kwon@naver.com'
# pw = 'qlqjs486!@!'


def summary(**args):
    
    id = instaemail.value
    pw = instapw.value
    
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(3)

    # 인스타그램 로그인
    driver.get('https://www.instagram.com/accounts/login/')

    time.sleep(random.randint(2,5))


    driver.find_element("name", 'username').send_keys(id)
    driver.find_element("name", 'password').send_keys(pw)
    time.sleep(random.randint(2,5))

    driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]').click()


    time.sleep(random.randint(2,5))


    # 팝업 창 1 제거
    driver.find_element("class name", "cmbtv").click()


    time.sleep(random.randint(2,5))


    # 팝업 창 2 제거
    driver.find_element("class name", "_a9--._a9_1").click()

    time.sleep(random.randint(2,5))

    # 개인 프로필 진입
    div = driver.find_element("class name","_aaav")
    btn= div.find_element("tag name",'img')
    btn.click()
    driver.find_element("class name", "_ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._aaay._abcm").click()

    time.sleep(10)





    # 3열로 나눠짐 3개씩


    indicator = driver.find_element("class name","_ac2a").text

    indicator = int(indicator)-15

    print("게시물 수:",indicator)

    time.sleep(random.randint(2,5))

    row_num = int(indicator)//3
    row_num_remain = int(indicator)%3


    if row_num_remain != 0:
        row_num += 1




    time.sleep(random.randint(2,5))

    # 게시물 클릭
    post_1 = driver.find_element("class name",'_aabd._aa8k._aanf')
    post_click = post_1.find_element("tag name", 'a').click()


    time.sleep(random.randint(2,5))


    def collertor(i,j):


        # 인사이트 클릭
        driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/div/section/button').click()
        time.sleep(random.randint(2,5))

        # 정보 수집
        like = driver.find_element("xpath",
                                '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div/div/div/div[1]/div[2]/span').text
        comment = driver.find_element("xpath",
                                    '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/div/div/div/div[2]/div[2]/span').text
        reach = driver.find_element("xpath",
                                    '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[7]/div/div/div/div[2]/div/span[1]').text
        exposure = driver.find_element("xpath",
                                    '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[7]/div/div/div/div[3]/span[2]').text
        date = driver.find_element("xpath",
                                '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[2]/div/div/a/div/time').text


        # 정보 저장
        sns_name.append('인스타그램')
        like_lst.append(like)
        comment_lst.append(comment)
        reach_lst.append(reach)
        exposure_lst.append(exposure)
        date_lst.append(date)

        # 인사이트 정보 닫기
        time.sleep(random.randint(2,5))
        driver.find_element("xpath",
                            '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[3]/div/button').click()


        # 다음게시물로 전환
        time.sleep(random.randint(2, 5))
        if(i+1!=row_num or j!=row_num_remain):
            span_next = driver.find_element("class name", "_aaqg._aaqh")
            next_button = span_next.find_element("tag name", 'button')
            next_button.click()
        elif(i+1==row_num and j==row_num_remain):
            driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div').click()


    # 함수 실행
    for i in range(0,row_num):
        print(i)
        if i != row_num:
            for j in range(1,4):
                collertor(i,j)
        elif i+1==row_num:
            if row_num_remain == 0:
                row_num_remain = 3
            for j in range(1,row_num_remain+1):
                collertor(i,j)


    ### 데이터 프레임 csv파일 형태로 저장

    # instagram_record = pd.DataFrame({'활동영역': sns_name,
    #                                '노출': exposure_lst,
    #                                    '도달': reach_lst,
    #                                    '공감': like_lst,
    #                                    '댓글': comment_lst,
    #                                '게시일':date_lst})

    # instagram_record.to_csv('C:/Users/USER/Desktop/instagram.csv',encoding='cp949')

    results.element.innerText = exposure_lst




