import urllib.request


url = 'https://www.daelim.ac.kr/type/KOR_A/img/intro/logo.png'
# v 0.1
# try:
# 	urllib.request.urlretrieve(url=url, filename="./img/dealim.png")  # 보조기억장치(HDD)에 저장
# 	print('성공')
# except Exception as e:
# 	print('실패')

# v 0.2
logo = urllib.request.urlopen(url=url).read()  # 메모리(Ram)에 저장

with open('./img/logo.png', 'wb') as file:  # wb -> Write Binary
	file.write(logo)
	print('저장 완료')
