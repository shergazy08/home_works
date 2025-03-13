def func():
    print("python")
    print("java")
    print("c++")
    print("#" * 10)


def area_circle():
    rad=float(input("radius: "))
    s=3,14*rad ** 2
    print("ai=",s)

def area_sher(width,height):
    if width < 0 or height < 0:
        print("tersa bolboit")
    else:
        area=width*height
        print("aiat=",area)

area_sher(10,11)


def info(shergazy):
    print(f"your name is {shergazy}")

aty=input("name: ")
info(aty)
