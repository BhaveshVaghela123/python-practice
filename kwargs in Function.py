def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)


student_info(name="Bhavesh", age=20, city="Ahmedabad")