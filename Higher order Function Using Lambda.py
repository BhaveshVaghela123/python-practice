def calculate(func, number):
    return func(number)


result = calculate(lambda x: x * 2, 10)

print(result)
