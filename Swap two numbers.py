# Swap two numbers
a = int(input("Enter the value of first number:"))
b = int(input("Enter the value of second number:"))
print("Before swapping: a =", a, "b =", b)
temp = a
a = b
b = temp
print("After swapping: a =", a, "b =", b)