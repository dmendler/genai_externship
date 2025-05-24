person = {
    "name": "Danny",
    "age": 21,
    "city": "Philadelphia",
}

person["favorite color"] = "Blue"

person["city"] = "New York"

print("Keys:", ", ".join(person.keys()))
print("Values:", ", ".join(map(str, person.values())))