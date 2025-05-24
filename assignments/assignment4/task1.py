fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Original list: {fruits}")

fruits.append('fig')
print(f"After adding a fruit: {fruits}")

fruits.remove('apple')
print(f"After removing a fruit: {fruits}")

fruits = fruits[::-1] # reverse order
print(f"Reversed list: {fruits}")