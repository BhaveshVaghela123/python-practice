
class Student:
    college = "New LJIET"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("College:", Student.college)


s1 = Student("Bhavesh")
s2 = Student("Rahul")

s1.display()
print("----------")
s2.display()
