from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 브라우저 생성
browser = webdriver.Chrome(options=chrome_options)
browser.get(
    'https://www.adiga.kr/PageLinkAll.do?link=/kcue/ast/eip/eis/inf/univinf/eipUinfMainGnrl.do&p_menu_id=PG-EIP-01801&univ_cd=0000063')

# 동적 로딩으로 늦게뜨는 컨텐츠들을 확인하기위해 강제로 5초 쉬기
time.sleep(5)

text = browser.find_element(By.CLASS_NAME, 'd_list_box').text

print(text)
