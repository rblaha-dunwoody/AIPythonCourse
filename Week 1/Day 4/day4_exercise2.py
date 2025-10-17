sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Initialize a Dictionary
word_count = {}

# Count word frequency
for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)