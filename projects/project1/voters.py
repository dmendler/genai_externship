# Get the user's age
age = int(input("How old are you? "))

if age >= 18:   # Check if the user is old enough to vot (18)
    print("Congratulations! You are eligible to vote. Go make a difference!")
else: # If not, print how many years they have left to be eligible and print a message
    yrs = 18 - age
    print(f"Oops! You are not eligible yet. But hey, only {yrs} years to go!")