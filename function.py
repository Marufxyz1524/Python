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

def show(n):
    if(n==0):
     return
    print(n)        
    show(n-1)
    print("END")
show(3)        
