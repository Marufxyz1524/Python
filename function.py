# def calc_sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum

# calc_sum(10, 20)
# calc_sum(20,30)
# #  shrt method
# sum = calc_sum(a,b)
# print(sum)
# return sum

# def prod(a , b=2):
#     m = a * b
#     print(m)
#     return m
# prod(2)

# n = 5
# fact = 1 

# for i in range(1 , n+1):
#      fact *= i 
# print(fact)  ## output only 120
#     #  print(fact)output 1,2___120

# def cal_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
# cal_fact(6)        

# def show(n):
#     if(n==0):
#      return
#     print(n)        
#     show(n-1)
#     print("END")
# show(3)        

# def fact(n):
#     if(n==0 or n== 1):
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(4))

def calc_sum(n):
    if(n==0):
        return 0
    else:
        return calc_sum(n-1) + n
print(calc_sum(5))    
