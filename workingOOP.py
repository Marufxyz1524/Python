class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    def show_info(self):
        print("Name:", self.name)
        print("ID:", self.student_id)
        print("Department:", self.department)

    def study(self, subject):
        print(self.name, "is studying", subject)

    def result(self, marks):
        if marks >= 40:
            print(self.name, "has passed.")
        else:
            print(self.name, "has failed.")


student1 = Student("Maruf", "253001", "Software Engineering")
student2 = Student("Rahim", "253002", "Software Engineering")

student1.show_info()
student1.study("PYTHON")
student1.result(85)

print()

student2.show_info()
student2.study("DATABASE")
student2.result(35)