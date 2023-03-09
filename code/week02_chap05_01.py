letters = 'abcdefghijklmnopqrstuvwxyz'
# split => str -> list | default = space
daelim = 'Daelim University'.split('i')
tasks = 'get gloves,get mask,give cat vitamins,call ambulance'

print(daelim)
print(tasks.split(','))

print(letters[1:])
# == print(letters[:28])
print(letters[:-1])
print(letters[8:15])
print(str(letters[8:15])[::-1])