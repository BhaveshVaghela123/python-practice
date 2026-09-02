def total_marks(math, python, c):
    total = math + python + c
    return total


math = int(input("Enter Math marks: "))
python = int(input("Enter Python marks: "))
c = int(input("Enter C marks: "))

total = total_marks(math, python, c)

print("Total Marks =", total)