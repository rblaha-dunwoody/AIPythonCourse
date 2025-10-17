# Simple reading from files - could also just readline() or readlines()
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Writing to file    
with open("sample.txt", "w") as file:
    file.write("Hello, World!")
    file.writelines(["Alice", "Bob", "Cherry"])

# File is automatically closed
try:
    with open("sample.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File Not Found!")