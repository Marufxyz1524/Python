# list = [20,0,10,30]

# result = list[0] // list[1]

# print(result)

try:
    list = [20,0,10,30]
    result = list[0] // list[5]
    print(result)

except ZeroDivisionError:
    print("Not divisable by zero")

except IndexError:
    print("Index error : Index not available..")    
