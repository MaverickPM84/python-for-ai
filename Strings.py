#String Manipulation in Python

#f strings

#f strings are very imp in AI because they allow us to easily format strings with variables and expressions, making it easier to create dynamic messages and outputs.

#AI models often need to generate text based on variable data, and f strings provide a convenient way to do this.

name = "Alice"

print(f"Hello, {name}!")  # Output: Hello, Alice!

print(f"Hello", name)

#What is the difference between f strings and regular strings in Python?
#f strings allow for inline variable interpolation, making it easier to include variable values directly within the string. Regular strings require concatenation or formatting methods to achieve the same result.

#another example of f strings

age = 30
print(f"{name} is {age} years old.")  # Output: Alice is 30 years old.

#String methods

name = " Preetam "

name_lower = name.lower()
print(name_lower)  # Output: preetam

name_upper = name.upper()
print(name_upper)  # Output: PREETAM

name_stripped = name.strip()
print(name_stripped)  # Output: Preetam

name_replaced = name.replace("e", "a")
print(name_replaced)  # Output: Praetam

name_split = name.split("e")
print(name_split)  # Output: [' Pr', 'tam ']

name_index = name.index("e")
print(name_index)  # Output: 2

name_count = name.count("e")
print(name_count)  # Output: 2

sentence = "Hello, welcome to the world of AI."

sentence_title = sentence.title()
print(sentence_title)  # Output: Hello, Welcome To The World Of Ai.

sentence_capitalize = sentence.capitalize()
print(sentence_capitalize)  # Output: Hello, welcome to the world of ai.

sentence_find = sentence.find("Hello")
print(sentence_find)  # Output: 7

#Cleaning strings using string methods

messy = "   Hello, AI World!   "
print(messy.strip())  # Output: Hello, AI World!, removes leading and trailing whitespace

price = "Price: $100"
print(price.strip("$")) # Output: Price: 100, removes the $ sign

data = "name,age,location"
print(data.split(","))  # Output: ['name', 'age', 'location'], splits the string into a list

text = "The quick brown fox"
print(text.replace("fox", "AI model"))  # Output: The quick brown AI model

info = "Name: John Doe"
print(info.index("John"))  # Output: 6, finds the starting index of "John"

#Finding and replacing substrings

message = " I love Python programming with Python"

# Check if soemthing exists

print("Python" in message)  # Output: True
print("Java" in message)    # Output: False
print(message.startswith("I"))  # Output: True
print(message.endswith("Python"))  # Output: True

# FInd position

print(message.find("Python"))  # Output: 7 (first occurrence)
print(message.rfind("Python"))  # Output: 29 (last occurrence)

print(message.count("Python"))  # Output: 2

# Replace substring

new_message = message.replace("Python", "Javascript")
print(new_message)  # Output:  I love Javascript programming with Javascript


#for loop to iterate through each character in a string

text = "AI is the future"
for char in text:
    print(char)

# for loop exampples

fruits = "apple,banana,cherry"
fruit_list = fruits.split(",")
for fruit in fruit_list:
    print(fruit)

# another example for loop

sentence = "Data Science is amazing"
words = sentence.split(" ")
for word in words:
    print(word)

# while loop to iterate through each character in a string

message = "Hello, AI!"
index = 0
while index < len(message):
    print(message[index])
    index += 1

# while loop example

text = "Machine Learning"
index = 0
while index < len(text):
    print(text[index])
    index += 1

# Tips to remember for for loops and while loops

# Use for loops when you know the number of iterations or when iterating over a collection.
# Use while loops when the number of iterations is uncertain and depends on a condition.
# Ensure that the loop condition in while loops will eventually become false to avoid infinite loops.

# Use descriptive variable names for loop counters and iterators to enhance code readability.
# Use break and continue statements judiciously to control loop execution flow.
# Always test loops with different input scenarios to ensure they behave as expected.
# Use enumerate() in for loops when you need both the index and the value from a collection. 
# For example:  for index, value in enumerate(collection):      
# This provides a cleaner and more Pythonic way to access both the index and the value.

#Mental Models for - for loops and while loops
# For Loops: Think of a for loop as a conveyor belt in a factory. 
# Each item (element) on the belt is processed one by one in a systematic manner.
# You know exactly how many items are on the belt, and you process each item until you reach the end.

# While Loops: Imagine a while loop as a game where you keep playing until you reach a certain score.
# You don't know how many rounds it will take to reach that score, so you keep playing as long as your current score is below the target.
# The loop continues until the condition (current score < target score) is no longer true.

#Common mistakes to avoid
# Infinite Loops: Ensure that the condition in while loops will eventually become false.