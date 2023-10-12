import urllib.request

url = 'https://www.daelim.ac.kr/type/KOR_A/img/intro/logo.png'

try:
	urllib.request.urlretrieve(url=url, filename="./img/dealim.png")
	print('성공')
except Exception as e:
	print('실패')

