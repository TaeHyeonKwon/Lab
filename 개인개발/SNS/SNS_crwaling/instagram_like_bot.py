import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

instagram_tag = "영상편집"

# 수요일 영상제작
# 목요일 영상편집



like_cnt = 0
target = 100
# comment_lst = ['잘 보고 갑니다!','팔로우 신청합니다 (:','유익한 피드네요 도움이 많이 됐습니다!']

# ID / PW 입력
id = 'studiohollin@naver.com'
pw = 'ghffls2020!'



# 크롬드라이버 로드
driver = webdriver.Chrome('chromedriver.exe')

# 인스타그램 로그인
# driver.get('https://www.instagram.com/accounts/login/')
driver.get('https://instagram.com')

time.sleep(random.randint(2,5))

driver.find_element("name", 'username').send_keys(id)
driver.find_element("name", 'password').send_keys(pw)
driver.find_element("xpath", '//*[@id="loginForm"]/div/div[3]').click()

time.sleep(5)


# 팝업 창 1 제거
driver.find_element("class name", "cmbtv").click()


time.sleep(5)

# 팝업 창 2 제거
driver.find_element("class name", "_a9--._a9_1").click()

time.sleep(random.randint(2,5))


driver.get('https://www.instagram.com/explore/tags/{}/'.format(instagram_tag))

time.sleep(5)

# 초기 게시물 진입
post_1 = driver.find_element("class name",'_aabd._aa8k._aanf')
post_click = post_1.find_element("tag name", 'a').click()


while True:



    time.sleep(random.randint(2,5))

    ##################### 자동 좋아요 기능 ######################
    span = driver.find_element("class name","_aamw")
    like_btn = span.find_element("tag name",'button')
    btn_svg = like_btn.find_element("tag name",'svg')
    svg = btn_svg.get_attribute('aria-label')

    if svg == '좋아요':
        like_btn.click()
        like_cnt += 1
        print("{}번째 좋아요를 눌렀습니다.".format(like_cnt))
        # time.sleep(random.randint(2,5))


    else:
        print("이미 작업한 피드입니다.")
        # time.sleep(random.randint(2,5))


    # ##################### 자동 팔로우 기능 ######################
    #
    # span_follow = driver.find_element("class name","_aar2")
    # follow_btn = span_follow.find_element("tag name",'button')
    # follow_txt = follow_btn.text
    #
    # if follow_txt == '팔로우':
    #     follow_btn.click()
    #     print("해당 계정을 팔로우 합니다.")
    #     time.sleep(random.randint(2,5))
    #
    # elif follow_txt == '팔로잉':
    #     print("이미 팔로우한 계정입니다.")
    #     time.sleep(random.randint(2,5))

    # #################### 자동 댓글 기능 ##########################
    #
    # comment_blank=driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
    # comment_blank.click()
    #
    # time.sleep(random.randint(2,5))
    #
    #
    # input_blank = driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
    # message = random.choice(comment_lst)
    # input_blank.send_keys(message)
    # time.sleep(random.randint(2,5))
    #
    #
    # span_post_btn = driver.find_element("class name","_acan._acao._acas")
    # span_post_btn.click()
    #
    # print("댓글을 남겼습니다.")

    ############################################################

    # 다음게시물로 전환
    span_next = driver.find_element("class name","_aaqg._aaqh")
    next_button = span_next.find_element("tag name",'button')
    next_button.click()

    if like_cnt == target:
        driver.close()
        break

print("작업 끝!")






