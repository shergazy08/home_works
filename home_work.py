# def main( name,age):
#     return f'pribet, mene zobut {name}, mne {age} LET'
#
# print(main(name='shergazy',))
#
# '''
# main(name='shergazy')
# main('shergazy')
# def main(name='shergazy')
# '''

# def custom_sum(*args):
#     return sum(args)
#
# print(custom_sum(2,3,4,5,6,6,7,7,8,8))

# def pr_info(**kwarks):
#     for key, value in kwarks.items():
#         print(f'{key}: {value}')
#
# pr_info(name='shergazy', age=25, city='moskb')
# pr_info(width=20, hight=20)

def create_profile(*hobbies, **info):
    print(f"Хобби: {hobbies}")
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile("чтение", "спорт", name="Иван", age=30)


