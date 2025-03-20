# try:
#    a=int(input())
#    b=int(input())
#    c=a/b
#    print(c)
# # except ZeroDivisionError:
# #     print("bolso bolboit")
# # except ValueError:
# #     print("canga bolboit")
# except Exception:
#     print("kata bar")
from softwareproperties.gtk.utils import retry

# def is_date(day,month,year):
#     from datetime import date
#     try:
#         return date(year,month,day)
#     except ValueError:
#         return "kalendarda nyndai gok"
# print(is_date(18,3,2025))
# print(is_date(29,2,2025))

numbers=[1,2,3,4,5]
def indexs():
    try:
        a = int(input("san gaz: "))
        return numbers[a]
    except IndexError:
        return "myndai indexs gok"
    except Exception:
        return "kata bar"

print(indexs())






