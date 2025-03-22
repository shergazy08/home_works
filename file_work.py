# with open('file.txt', 'w') as file:
#     file.write('hello, world')
#
#
# with open('file.txt', 'w') as file:
#     file.write('\nthis is a new file')
#
#
# with open('file.txt', 'r') as file:
#     content = file.read()
#     print(content)
#
#
#
# with open("file.txt",'w+') as file:
#     file.write('Hello,ernis! \n Tb=his is a new line.')
#     file.seek(0)
#     content = file.read()
#     print(content)

with open('numbers.txt', 'w') as file:
    for i in range(5):
        a = int(input("gaz: "))
        file.write(f'a + \n')

with open('numbers.txt', 'r') as file:
    content = file.read()
    print(content)




