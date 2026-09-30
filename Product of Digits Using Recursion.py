def product_digits(n):
    if n == 0:
        return 1

    digit = n % 10

    return digit * product_digits(n // 10)


num = int(input("Enter a number: "))

result = product_digits(num)

print("Product of digits =", result)