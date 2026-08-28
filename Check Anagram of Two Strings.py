text1 = input("Enter first string: ").replace(" ", "").lower()
text2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(text1) == sorted(text2):
    print("Anagram")
else:
    print("Not Anagram")