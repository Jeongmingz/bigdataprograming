# # List Comprehension
# numbers = []
# for i in range(1, 10, 3):
#     numbers.append(i**2)
#
# print(numbers)
#
# numbers = [i**2 for i in range(1, 10, 3)]
# print(numbers)

numbers = []

numbers = [i**2 for i in range(1, 10) if i % 2 == 0]
print(numbers)