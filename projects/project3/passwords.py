password = input("Enter a password: ")
flag = 1
score = 0

# either prints error message or adds 2 to score
if len(password) < 8: # checking length
    print("Password must be at least 8 characters long.")
    flag = 0
else:
    score += 2

if not any(c.isupper() for c in password): # checking uppercase
    print("Password must contain at least one uppercase letter.")
    flag = 0
else:
    score += 2

if not any(c.islower() for c in password): # checking lowercase
    print("Password must contain at least one lowercase letter.")
    flag = 0
else:
    score += 2

if not any(c.isdigit() for c in password): # checking digit
    print("Password must contain at least one digit.")
    flag = 0
else:
    score += 2

if not any(c in "!@#$%^&*()-_=+[]{};:,.<>?/" for c in password): # checking special character
    print("Password must contain at least one special character.")
    flag = 0
else:
    score += 2

# if password passes all checks, print success message and score
if flag:
    print("Your password is strong! 💪, you get a score of", score)

