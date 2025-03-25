# sad=lambda a, b: a +b
# print(sad(1,4))
#
# sd=lambda a: a
# print(sd('hello, worlld'))
#
# df=lambda:'hello'
# print(df())

numbers=[1, 2, 3, 4, 5]
gh=list(map(lambda x: x ** 2,numbers))
print(gh)

numbers=[10, 15, 20, 25, 30]
sh=list(filter(lambda x: x % 2 == 0,numbers))
print(sh)



lenght = lambda x: len(x)
print(lenght('python'))


numbers = [1, 2, 3, 4, 5]
s = list(map(lambda x: x * 3, numbers))
print(s)


words = ["кот", "машина", "птица", "слон", "компьютер"]
filtered_words = list(filter(lambda x: len(x) > 5,words))
print(filtered_words)

s=['iablaco','ananas','grusha','banan']
a=sorted(s, key=lambda x: len(x))
print(a)