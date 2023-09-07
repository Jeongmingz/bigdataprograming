acme_customer = dict(first='Wile', middle='E', last='Coyote')

print(acme_customer)

print(acme_customer.get('hello'))


word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)