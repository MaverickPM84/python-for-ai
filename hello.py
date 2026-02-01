# Let's explore variables

#variables are like containers that store data values.

name = "Preetam Kale"
print(f"Hello, {name}!")

# Some data to work with
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Calculate something
total = sum(numbers)
print(f"Total: {total}")

age = 30

age = 35  # Updating the age variable

#you can update the value stored in a variable by assigning a new value to it.

is_student = True
print(f"Is student: {is_student}")

#you can also store boolean values in variables.

#Naming Rules:
# 1. Variable names must start with a letter or an underscore (_).
# 2. The rest of the name can contain letters, numbers, and underscores.
# 3. Variable names are case-sensitive (age and Age are different variables).
# 4. Avoid using Python reserved words (like print, if, else, etc.) as variable names.

# Example of invalid variable names:
# 1. 2nd_name = "John"  # Starts with a number
# 2. first-name = "Doe"  # Contains a hyphen
# 3. class = "Math"      # Uses a reserved word

#Allowed variable names: keep it simple use snake_case
first_name = "John"
last_name = "Doe"

#Use descriptive names for your variables to make your code more readable. Instead of x or temp,
# use names like total_score or user_age that clearly indicate what the variable represents.

user_age = 25

#comments are lines that start with a # symbol. They are not executed as part of the code.
# Comments are used to explain the code and make it more understandable for others (or yourself in the future).
# Always strive to write clear and understandable code, and use comments to clarify complex parts when necessary.
print(f"User age: {user_age}") #printing user age

#multiple line comments can be done using triple quotes
# keyboard shortcut for multi-line comments is Ctrl + /
"""This is a multi-line comment.
It can span multiple lines.
Use it to explain complex code or provide detailed information."""

# When to use comments:
# Good comments explain WHY, not WHAT:"""

# Good comments example: Good explains WHY
# Using 1.0625 because sales tax in CA is 6.25%
# We multiply by 1.0625? To include sales tax in the total price. 
# When you want to increase a number by some percentage, you multiply by (1 + percentage/100).
#6.25% = 6.25/100 = 0.0625
#Add that to 1(which represents the original 100% of the price) 1+ 0.0625 = 1.0625

price = 70
total_price = price * 1.0625
print(f"Total price with tax: {total_price}")