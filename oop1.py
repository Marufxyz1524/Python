##basic class object
# class Student:
#     name = "Maruf"

# s1 = Student()
# print(s1.name)  
class Student:
        
   def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
s1= Student("Maruf",15,"SWE")        
print(s1.name,s1.age,s1.department)
s2= Student("Nahid",15,"CWE") 
print(s2.name,s2.age,s2.department)


