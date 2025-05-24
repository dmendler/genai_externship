intrests = ("Django", "No Pole", "Hunger Games")
print(f"Favorite things: {intrests}")

try:
    intrests[0] = "Star Wars"
except TypeError:
    print("Oops! Tuples cannot be changed.")

print(f"Length of tuple: {len(intrests)}")