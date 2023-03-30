# zip

eng = 'hello', 'bye', 'good'
kor = '안녕', '잘가', '좋다'

engkor_list = list(zip(eng, kor))
engkor_dict = dict(zip(eng, kor))

print(engkor_list, engkor_dict, sep='\n')