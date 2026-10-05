def smallest_digit(n):
    if n < 10:
        return n

    digit = n % 10
    smallest = smallest_digit(n // 10)

    if digit < smallest:
        return digit
    else:
        return smallest


num = int(input("Enter a number: "))

result = smallest_digit(num)

print("Smallest digit =", result)