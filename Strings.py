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