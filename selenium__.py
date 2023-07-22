from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def play_ted(url):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)

    # TED 영상 실행
    video_element = driver.find_element(By.CSS_SELECTOR, '.css-1oyuzmv')
    video_element.click()

    time.sleep(10)
    driver.quit()


play_ted('https://www.ted.com/talks/young_ha_kim_be_an_artist_right_now?language=ko')
