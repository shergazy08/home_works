res=[i for i in range(1,20)]
print(res)

res=[i ** 2 for i in range(1,11)]
print(res)

numbers=[5, 12, 7, 18, 3, 10, 8]
res=[n for n in numbers if n > 7]
print(res)

number=["яблоко", "банан", "вишня"]
res=[i for i in number]
print(res)

m=int(input("gaz: "))
res="on"if m > 0 else  "ters"
print(res)

n=int(input("gaz: "))
res="gup san" if n % 2 == 0 else "tak"
print(res)

m=[4, -1, 7, -3, 0, 9, -2]
res=[i if i >= 0 else 0 for i in m]
print(res)