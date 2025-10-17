# Syntax for 'for' loop
""" for item in sequence:
    # Code block """

# Syntax for 'while' loop
""" while True:
    # Code block """

# Example 1: Checking a condition
""" num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number") """
    
# Example 2: Nested conditions
""" age = 5
if age > 18:
    if age < 30:
        print("Young adult")
    else:
        print("Adult")
else:
    print("Child") """
    
# Example 3: Loop through a list
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

# Loop with range
for i in range(5):
    print(i)

# Example 4: While loop count down
count = 5
while count > 0:
    print(count)
    count -= 1
print("While loop completed")
