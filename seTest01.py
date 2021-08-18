#인터프리터 아나콘다를 설치 후 (환경 변수 설정+) 프로젝트와 연동
#conda install selenium
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome('/Users/ekxm2/PycharmProjects/chromedriver.exe')
#사용자 구글드라이브 경로에 따라 변경
driver.implicitly_wait(3)

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요? : ')
url = baseUrl + quote_plus(plusUrl)


driver.get(url)
driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
v = soup.select('.yuRUbf')
for i in v:
    print(i.select_one('.LC20lb.DKV0Md').text)
    print(i.a.attrs['href'])
    print()

driver.close()
