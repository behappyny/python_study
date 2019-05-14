import requests #웹 페이지에 접속할 때 필요한 모듈 임포트
from bs4 import BeautifulSoup #HTML을 해석할 때, 필요한 모듈

resp = requests.get('https://www.naver.com/')
soup = BeautifulSoup(resp.text, 'html.parser') #resp : 변수, 'html parser' : html을 추적한다
titles = soup.select('.ah_roll .ah_k')  # 타이틀(제목)을 가지고 있는 클래스 명
                                        #클래스명 ah_roll의 자손인 ah_k 클래스 선택, 자손요소를 선택할 때는 한칸 띄기

for i, title in enumerate(titles, 1):
    print(f'{i}위 {title.get_text()}')