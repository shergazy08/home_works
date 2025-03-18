from random import randint, choice

randint,choice


def computer_choice():
    return randint[1,10]


def user_choice():
    ch=int(input("gaz: "))
    return ch

def check(c_choice,u_choice):
    if c_choice == u_choice:
        return "ugadai"
    else:
        return "ne ugadai"




def main():
    while True:
        print("1. start")
        print("2. bytyr")
        ch =int(input("choocing: "))
        if ch == 1:
            while True:
                com_choice=computer_choice()
                us_choice=user_choice()
                if user_choice == -1:
                    print("tuura mmes")
                    continue
                    res=check(com_choice,us_choice)
                    print(res)
        elif ch == 2:
            break
        else:
            print("tuura mes")

main()