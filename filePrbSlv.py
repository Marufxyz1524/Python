# with open("data.txt","r") as file:
#    data = file.read()
#    numbers = data.split(",")

# count = 0

# for num in numbers:
#    if int(num) % 2 == 0:
#       print(int(num))
#       count += 1
# print("Even numbers:",count)   

##this prblm another way to solve:
with open("data.txt","r") as file:
     data = file.read()
     numbers = data.split(",")

even_num = []

for num in numbers:
     if int(num) % 2 == 0:
          even_num.append(int(num))
         
print("Even numbers are : ",even_num)
print("Total even number: ",len(even_num))          
