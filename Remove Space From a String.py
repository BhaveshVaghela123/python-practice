text = input("Enter a string: ")

new_text = ""

for char in text:
    if char != " ":
        new_text += char

print("String without spaces =", new_text)