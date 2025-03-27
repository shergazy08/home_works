# numbers = [x for x in range(5)]
# print(numbers)
# # for i in numbers:
# #     print(i)
# numbers = []
# for x in range(5):
#     numbers.append(x)
#
#
# even_numbers = [x for x in range(10) if x % 2 == 0]
# print(even_numbers)
#
#
# words = ['apple', 'orange', 'cherry']
# short_words = [word.upper() for word in words]
# print(short_words)
#
# numbers = tuple(x for x in range(100))
# print(numbers)
#
#
# words = ["cat", "elephant", "dog", "giraffe"]
# lengths = [len(word) for word in words]
# print(lengths)

words = ['apple', 'banana', 'avocado', 'cherry', 'apricot',]
filtered_words = [word for word in words if word.startswith('a')]
print(filtered_words)