# return - kaitaruu
from orca.messages import cellSpan


# def add(a, b):
#     print(a+b)
#     return a+b
#
# res=add(1,2)
# print(res)

def weather(celsius):
    if celsius < 0:
        return  "suuk"
    elif 0 < celsius < 20:
        return  "gyluu"
    else:
        return "ysyk"
# print(weather(-1))
