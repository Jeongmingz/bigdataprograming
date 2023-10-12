import urllib.request as request
import urllib.parse as parse


# url = 'https://www.daelim.ac.kr/type/KOR_A/img/intro/logo.png'
# v 0.1
# try:
# 	request.urlretrieve(url=url, filename="./img/dealim.png")  # 보조기억장치(HDD)에 저장
# 	print('성공')
# except Exception as e:
# 	print('실패')

# v 0.2
# logo = request.urlopen(url=url).read()  # 메모리(Ram)에 저장
#
# with open('./img/logo.png', 'wb') as file:  # wb -> Write Binary
# 	file.write(logo)
# 	print('저장 완료')

# v 1.0
# api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
#
# station_id = input('지역코드 : ')  # 108, 105, 109, 184
# values = {'stnId': station_id}
# parameters = parse.urlencode(values)
#
# url = api + '?' + parameters
#
# response = request.urlopen(url).read()
# datas = response.decode('utf-8')
# print(datas)

# v 1.1 use BS4
# from bs4 import BeautifulSoup
#
# html = """
# 	<html>
# 		<head>
# 			<title>스크레이핑 실습</title>
# 		</head>
# 		<body>
#
# 			<a href="www.daelim.ac.kr">대림대학교</a>
# 			<a href="www.harbard.edu">하버드</a>
#
# 			<h1>대림대학교</h1>
# 			<p>웹 스크레이핑</p>
# 			<p>파이썬 기본 문법, 넘파이, 판다스, 맷플롯립, 사이킷런, GUI ...</p>
# 		</body>
# 	</html>
# """
#
# soup = BeautifulSoup(html, 'html.parser')
# t = soup.html.head.title
# h1 = soup.html.body.h1
# # p1 = soup.html.body.p
# # p2 = p1.next_sibling.next_sibling
#
# p = soup.findAll('p')
# a = soup.findAll('a')
#
# print(t.text, h1.text,)
#
# for i in a:
# 	data = {'link': i.attrs['href'], 'univ_name': i.string}
# 	print(data)

# v 1.2 use BS4
from bs4 import BeautifulSoup
import urllib.request as request

api = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
response = request.urlopen(api).read()
soup = BeautifulSoup(response, 'html.parser')

citys = soup.findAll('city')
body = soup.find('body')
datas = body.findAll('data')
time = body.find('tmef').string

for i, city in enumerate(citys):
	print(city.string+"의\t"+time+"시의 날씨는 "+ datas[13*i].find("wf").string)

