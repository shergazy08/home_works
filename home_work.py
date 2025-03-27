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

# words = ['apple', 'banana', 'avocado', 'cherry', 'apricot',]
# filtered_words = [word for word in words if word.startswith('a')]
# print(filtered_words)

import time


a = 100


park = {}


def car():
    return str(int(time.time()))


def sad():
    car_number = input("Введите номер машины: ").strip().upper()


    if not car_number:
        print("Ошибка: Введите правильный номер машины.")
        return

    number = car()
    sd = time.time()
    park[number] = {"car_number": car_number, "entry_time": sd, "paid": False}

    print("\nТалон выдан:")
    print("Номер талона:", number)
    print("Номер машины:", car_number)
    print()


def return_():
    ticket_number = input(" номеr talon: ").strip()


    if ticket_number not in park:
        print("Ошибка: Талон не найден.")
        return

    if park[ticket_number]["paid"]:
        print("Ошибка: Талон уже оплачен.")
        return

    en= park[ticket_number]["entry_time"]
    ex = time.time()
    ho= int((ex - en) // 3600) + 1
    total = ho* a

    print("\nСчет к оплате:")
    print("Номер талона:", ticket_number)
    print("Номер машины:", park[ticket_number]["car_number"])
    print("Продолжительность парковки:", ho, "час(ов)")
    print("Стоимость парковки:", total, "сом")
    print()

    park[ticket_number]["paid"] = True


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Выдача талона")
        print("2. Сдача талона")
        print("3. Выход")

        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            sad()
        elif choice == "2":
            return_()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Неверный ввод, попробуйте снова.")


main()