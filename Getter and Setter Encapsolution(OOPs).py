
#Getter and Setter 
class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


s1 = Student("Bhavesh")

print("Old Name:", s1.get_name())

s1.set_name("Rahul")

print("New Name:", s1.get_name())
