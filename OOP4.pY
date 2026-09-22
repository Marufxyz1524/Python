class Student:
    def __init__(self,name,id,present,sallery,absent):
        self.name = name
        self.id = id
        self.present = present
        self.sallery = sallery
        self.absent = absent

    def your_name(self):
         print("Hello, Mr. ",self.name)

    def your_id(self):
         print("Your id is ",self.id) 

    def present_day(self):
         print("You present in your company ",self.present)

    def ur_sallery(self):
         print("So your saller is ",self.sallery)

    def u_absent(self):
        print("Cause you ABSeNt ",self.absent) 

person = Student("Maruf",220,120,23000,67)

person.your_name()
person.your_id()
person.present_day()
person.ur_sallery()
person.u_absent()
                         




         