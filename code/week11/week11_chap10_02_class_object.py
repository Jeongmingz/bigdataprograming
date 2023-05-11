# week11_chap10_02_class_object

from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')  # 속성은 space로 구별한다.
duck = Duck('wide orange', 'long')

print(duck)
print(f'뿌리 : {duck.bill}, 꼬리 : {duck.tail}')


parts = {'bill': 'wide blue', 'tail': 'short'}
duck2 = Duck(**parts)

print(duck2)
print(f'뿌리 : {duck2.bill}, 꼬리 : {duck2.tail}')


duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)
print(f'뿌리 : {duck3.bill}, 꼬리 : {duck3.tail}')
