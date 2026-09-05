class Student:
    def __init__(self,name,roll,subject):
        self.name = name
        self.roll = roll
        self.subject = subject

    def welcome(self):
        print("Welcome student",self.name)

    def show_roll(self):
        print("Your roll is",self.roll)

    def show_subject(self):
        print("Now you are studying in",self.subject)

s1 = Student("Maruf",3,"SWE")
s1.welcome()
s1.show_roll()
s1.show_subject()        
                
        