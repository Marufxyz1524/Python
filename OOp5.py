##creating dog class
class DOG:
 
      def __init__(self,name,age):
             self.name = name
             self.age  = age

      def sit(self):
             print(f"{self.name} in now sitting")

      def roll_over(self):
             print(f"{self.name} rolled over")

my_dog = DOG("Willie",6)
# print(f"My dog name is {my_dog.name} ")
# print(f"He {my_dog.age} years old")             
# my_dog.sit()
# my_dog.roll_over()
                   
       