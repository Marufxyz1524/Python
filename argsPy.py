# def sum(num1,num2):
#     result = num1 + num2
#     return result

# total = sum(99,45,100)
# print("Total",total)

##args
def all_sum(num1,num2,*numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum += num
    return sum
    
total = all_sum(45,46,89,67,45,67,78)
print("all sum: " , total)

