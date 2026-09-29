def count_digits(n):
    if n == 0:
        return 0

    return 1 + count_digits(n // 10)


num = int(input("Enter a number: "))

if num == 0:
    count = 1
else:
    count = count_digits(num)

print("Number of digits =", count)