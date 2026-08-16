num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0 or num == 1:
    print("Factorial =", 1)
else:
    for i in range(2, num + 1):
        factorial *= i
print("Factorial =", factorial)