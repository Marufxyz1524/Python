# num2 = int(input("Enter your numbers: "))
# if(num2 == 0):
#     print("Not divisable")
# else:
#  result = int(20 / num2)
# print(result)

##this prblm should follow excption hndling
## ata chara kkhnoi perfect hbena

try:
    num2 = int(input("Enter your numbers: "))
    result = 20 // num2
    print(result)

except ZeroDivisionError:
    print("Not divisable by zero")


