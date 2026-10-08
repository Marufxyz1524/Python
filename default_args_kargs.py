# def sum(num1,num2):
#     result = num1 + num2
#     return result

# total = sum(35,56)  ##(36,67,78) gives default parameter 
# print("Total",total)

def all_sum(num1 , num2 , *numbers):
    sum = 0
    for num in numbers:
        print(num)
        sum += num
    return sum
total = all_sum(3,5,7,1,8,7,4)
print("Total Sum: ",total)        