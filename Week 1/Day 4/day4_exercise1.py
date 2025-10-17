person = {"name": "Alice", "age": 25, "grade": "A"}
print(person)

# Add a new key-value pair
person["address"] = "123 Main St"

# Update age
person["age"] = 32

# Remove grade
if "grade" in person:
    del person["grade"]

print(person)