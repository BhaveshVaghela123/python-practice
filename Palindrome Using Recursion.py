def reverse_number(n, reverse=0):
    if n == 0:
        return reverse

    digit = n % 10
    reverse = reverse * 10 + digit

    return reverse_number(n // 10, reverse)


num = int(input("Enter a number: "))

reverse = reverse_number(num)

if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")