import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawling():
    url = 'https://www.ted.com/talks/young_ha_kim_be_an_artist_right_now/transcript?language=ko'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #response = requests.get(url).text에서 자막이 담긴 부분 찾음
    divs = soup.find('script', {"type": "application/json"})
    div = json.loads(divs.text) #자막 부분을 값을 효율적으로 찾기 위해 str -> dict 형태로 바꿈

    srt = []
    num = 1
    for i in div["props"]["pageProps"]["transcriptData"]["translation"]["paragraphs"]:
        for j in i['cues']:

            #영상 시간 값 변환
            time_delta = pd.to_timedelta(int(j['time']), unit='ms')
            formatted_time = "{:02d}:{:02d}:{:06.3f}".format(
                time_delta.seconds // 3600,  # 시간
                (time_delta.seconds // 60) % 60,  # 분
                time_delta.seconds % 60 + time_delta.microseconds / 1000000  # 초 (밀리초 포함)
            )

            #추출한 값 리스트에 넣음
            if(num == 1):
                srt.append([num,str(formatted_time)+" --> ",j['text']])
            else:
                srt[num-2][1] += str(formatted_time)
                srt.append([num, str(formatted_time) + " --> ",j['text']])

            num += 1

    return srt

def create_srt(lst):
    with open("ted.srt", 'w', encoding='utf-8') as f:
        for num, time, text in lst:
            f.write(f"{num}\n")
            f.write(f"{time}\n")
            f.write(f"{text}\n")
            f.write("\n")


create_srt(crawling())

