
class Student:
    college = "New LJIET"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

    def display(self):
        print("College:", self.college)


s1 = Student()
s1.display()

Student.change_college("IIT Bombay")

s1.display()
