# Exercise 1: Create a text cleaner
import re

def clean_text(text):
    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    text = " ".join(text.split())
    # Conver to lower case
    return text.lower()

input_text = "     Hello, World!!! Welcome to Python, Programming....      "
cleaned_text = clean_text(input_text)
print("Cleaned text: ", cleaned_text)


# Exercise 2: Check if a string is a palindrome
def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_text = input("Enter a string: ")
if is_palindrome(input_text):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome")