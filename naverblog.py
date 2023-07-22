import requests
from bs4 import BeautifulSoup


def blog_crawling():
    subject = []
    url = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%ED%99%8D%EB%8C%80+%EB%A7%9B%EC%A7%91'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #블로그 이름만 추출함
    divs = soup.findAll('span', {"class": "elss etc_dsc_inner"})
    print("div는",divs)

    for div in divs:
        links = div.findAll('a')

        for link in links:
            subject.append(link.text)

    return subject

print(blog_crawling())