class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

    def intoduce(self):
        print(f"I am {self.name} and {self.age} years old")

class Employee(Person):
    def __init__(self,name,age,sallery,dept):
        super().__init__(name,age)
        self.sallery = sallery
        self.dept = dept

    def intoduce(self):
        super().intoduce()
        print(f"I work in {self.dept} and earn {self.sallery} USD in year")

e = Employee("Maruf" , 21 , 30000, "DevOps")
e.intoduce()

