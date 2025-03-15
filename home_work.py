from random import randint, choice

from defer import return_value
from softwareproperties.gtk.utils import retry


def computer_choice():
    return choice(['kamen', 'nog', 'bumaga'])


def user_choice():
    print('1. kamen')
    print('2. nog')
    print('3. bumaga')

    ch = int(input("tanda: "))
    if ch == 1:
        return "kamen"
    elif ch == 2:
        return "nog"
    elif ch == 3:
        return "bumaga"
    else:
        return -1


def check(c_choice, u_choice):
    if c_choice == u_choice:
        return 'nichi'
    elif c_choice == 'kamen' and u_choice == 'nog':
        print(f"computer: {c_choice} - user: {u_choice}")
        return 'progral'
    elif c_choice == 'nog' and u_choice == 'bumaga':
        print(f"computer: {c_choice} - user: {u_choice}")
        return 'utul'
    elif c_choice == 'bumaga' and u_choice == 'kamen':
        print(f"computer: {c_choice} - user: {u_choice}")
        return 'utrul'
    else:
        print(f"computer: {c_choice} - user: {u_choice}")
        return 'ura win'





