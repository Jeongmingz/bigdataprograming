# week04_chap08_01.py
# Dictionary Comprehensions

word1 = 'letter'
letter_counts1 = {letter: word1.count(letter) for letter in word1}
letter_counts2 = {letter: word1.count(letter) for letter in set(word1)}
print(letter_counts1)

vowels = 'aeiou'
word2 = 'onomatopoeia'
vowel_counts = {letter: word2.count(letter) for letter in word2 if letter in vowels}
print(vowel_counts, end='\n\n')

mobile_phone = {0, 1, 0, 3, 3, 3, 7, 0, 8, 6, 1}
print(type(mobile_phone), mobile_phone)

a = {1, 2}
b = {2, 3}
print(a <= b)
fs = frozenset(a)
print(fs)