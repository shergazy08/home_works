from home_work import computer_choice, user_choice, check


def main():
    while True:
        print("1. nachat")
        print("2. buiti")

        ch=int(input("tanda"))
        if ch == 1:
            while True:
                com_ch=computer_choice()
                us_ch=user_choice()
                if us_ch == -1:
                    print("tuura mes")
                    continue
                res=check(com_ch,us_ch)
                print(res)
        elif ch == 2:
            break
        else:
            print("tuura nes")

main()