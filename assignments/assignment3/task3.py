s = input("Enter a word: ")
temp = s.lower()
s_reversed = temp[::-1]
if temp == s_reversed:
    print(f"Yes, '{s}' is a palindrome!")
else:
    print(f"No, '{s}' is not a palindrome.")