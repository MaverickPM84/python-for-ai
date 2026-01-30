""" All programming boils down to a few basic operationss. This module covers them all.
Programming is all about giving precise instructions to a computer to perform specific tasks.

Computers are literal. 
If you as a person to make a sandwich, you might say "make me a sandwich with lettuce, tomato, and cheese".

A computer needs you to be more specific. 
It needs to know exactly what type of bread, how much lettuce, how to slice the tomato, and what type of cheese.
Every single step needs to be spelled out in detail."""

#Few Basic Operations in Python

#Store Information

age = 25  # Storing an integer value
name = "Alice"  # Storing a string value

#We can reference these values later in the program
print(f"{name} is {age} years old.")  # Output: Alice is 25 years old.

#Make Decisions

if age >= 18:
    print(f"{name} is an adult.")
else:
    print(f"{name} is a minor.")

#Repeat Actions

"""repeat 10 times:
    do pushups"""

for i in range(5):
    print(f"Doing pushups: {i+1}")

#Perform Calculations

# total = price + tax

#Python Syntax
#Rules for indentation, naming conventions, and structure of statements

#Indentation rules
def greet_user(username):
    print(f"Hello, {username}!")  # Indented block inside the function. 4 spaces not tabs.

#Python style guide PEP8
#Use 4 spaces per indentation level, not tabs.
#Naming Convention - Use lowercase with underscores for variable and function names
#Limit lines to 79 characters for better readability
#Use blank lines to separate functions and classes for better organization
#Use comments to explain complex code or logic
#Use docstrings to describe the purpose of functions and classes
#Where to add spaces around operators and after commas for better readability



#How to read error messages
"""Python errors have three parts:
Where it happened: File "hello.py", line 1
What went wrong: SyntaxError: unterminated string literal
The arrow: Points to the exact spot where the error occurred"""
#SyntaxError: Indicates a mistake in the code structure
#Example of a syntax error
#print("Hello, World!) # Missing closing quotation mark

print("Hello, World!") 