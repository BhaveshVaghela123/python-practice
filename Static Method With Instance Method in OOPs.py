
class Student:

    school = "ABC School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def is_pass(marks):
        return marks >= 40

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

        if Student.is_pass(self.marks):
            print("Result: PASS")
        else:
            print("Result: FAIL")


s1 = Student("Bhavesh", 85)
s2 = Student("Rahul", 30)

s1.display()
print("----------")
s2.display()
