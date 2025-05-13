s = "Python is amazing!"
first_word = s.split()[0]
amazing = s.split()[2][:-1]
s_reversed = s[::-1]

print(f"First word: {first_word}")
print(f"Amazing part: {amazing}")
print(f"Reversed string: {s_reversed}")