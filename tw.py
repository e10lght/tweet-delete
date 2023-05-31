from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()  
path = os.getenv('PROFILE_PATH')
personalization_id = os.getenv('PERSONALIZATION_ID')
guest_id = os.getenv('GUEST_ID')
twid = os.getenv('TWID')
auth_token = os.getenv('AUTH_TOKEN')
ct0 = os.getenv('CT0')

try:

    # 手動でログインして取得したクッキー
    cookies = [
        {'name': 'personalization_id', 'value': personalization_id},
        {'name': 'guest_id', 'value': guest_id},
        {'name': 'twid', 'value': twid},
        {'name': 'auth_token', 'value': auth_token},
        {'name': 'ct0', 'value': ct0},
    ]

    # ドライバーの設定
    driver = webdriver.Chrome(service=Service('./chromedriver'))
    driver.get('https://twitter.com/')

    # 手動で取得したクッキーをセット
    for cookie in cookies:
        driver.add_cookie(cookie)

    # クッキーをセットした後にページに再度アクセス
    url = f"https://twitter.com/{path}"
    driver.get(url)

    time.sleep(3)

    # 返信タブに移動
    replay = driver.find_elements(By.CSS_SELECTOR, '.css-1dbjc4n.r-16y2uox.r-6b64d0.r-cpa5s6')
    if len(replay) > 1:  
        fourth_element = replay[1] 
        fourth_element.click()
    else:
        print("Element not found or less than two elements")

    # 削除実行（リツイートは不可）
    for i in range(500):
        print(str(i)+"start")
        time.sleep(1)
        elements = driver.find_elements(By.CSS_SELECTOR, '.css-18t94o4.css-1dbjc4n.r-1777fci.r-bt1l66.r-1ny4l3l.r-bztko3.r-lrvibr')
        if len(elements) > 0:
            elements[0].click()
            time.sleep(1)
            delete = driver.find_elements(By.CSS_SELECTOR, '.css-1dbjc4n.r-1loqt21.r-18u37iz.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg.r-13qz1uu')
            delete[0].click()
            time.sleep(1)
            submit = driver.find_elements(By.CSS_SELECTOR, '.css-901oao.r-1awozwy.r-jwli3a.r-6koalj.r-18u37iz.r-16y2uox.r-1tl8opc.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0')
            submit[0].click()
            time.sleep(1)
        else:
            print("Element not found")

    input("Press any key to close the browser...")

except Exception as e:
    print(f"An error occurred: {e}")
