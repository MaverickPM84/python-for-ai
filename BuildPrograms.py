# Functions

# Create reusable blocks of code that do specific tasks.

#Think of functions as mini-programs within your program.

# They take inputs, process them, and return outputs.

# A recipe you can follow multiple times with different ingredients.

# A machine that takes input and produces output

# A named shortcut for complex operations.

# WHy use functions?

# Don't repeat yourself - Code Reusability: Write once, use multiple times.
# Stay Prganized - Break down complex problems into smaller, manageable pieces.
# Easy to Test and Debug - Isolate issues within specific functions.

# Defining functionas - create your own repeatable block of code -> Parameters and Arguments - Pass data to functions -> Return Values - get results from functions

# Real-world examples

# Functions are everywhere in programming. Here are some common examples:

#print() - Outputs text to the console.
#len() - Returns the length of a string, list, or other collection.
#input() - Gets user input from the console.
#str(), int(), float() - Convert data types.

# Custom Function Example
# calculate_tax() - Calculate sales tax for a given amount.
def calculate_tax(amount, tax_rate):
    """Calculate the sales tax for a given amount."""
    tax = amount * tax_rate
    return tax

#send_email() - Send an email notification.
def send_email(recipient, subject, body):
    """Send an email notification."""
    print(f"Sending email to {recipient} with subject '{subject}' and body '{body}'")

#Defining a function

def greet(name):
    print(f"Hello, {name}!")

#Calling a function

greet("Alice")  # Output: Hello, Alice!


#Naming functions

#Good names should be descriptive and follow conventions.

def calculate_tax(amount, tax_rate):
    return amount * tax_rate

def send_email(recipient, subject, body):
    print(f"Sending email to {recipient} with subject '{subject}' and body '{body}'")
    pass

def validate_password():
    pass

#Function with return value

def add(a, b):
    return a + b

# use lowercase with underscores to separate words (snake_case), be descriptive about what it does.

#calling function

result = add(5, 3)
print(result)  # Output: 8

#Function with parameters
def multiply(x, y):
    return x * y

product = multiply(4, 6)
print(product)  # Output: 24

def check_weather(temperature):
    
    if temperature > 30:
        return "It's hot outside!"
    else:
        return "It's a comfortable day."
    
weather_message = check_weather(40)
print(weather_message)  # Output: It's hot outside!


#multiple parameters

def calculate_compound_interest(principal, rate, time, compound_frequency):
    """Calculate compound interest."""
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    return amount - principal

interest = calculate_compound_interest(1000, 0.05, 2, 4)
print(interest)  # Output: 107.1875


#default parameter values
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Hi there!")  # Output: Hi there!, Bob


#Global variables can be accessed inside functions, but as a best practice, specify a variable locally within the function
#if you are using a variable inside a function, define it there or pass it as a parameter.

#Global variable can be accessed inside functions, but local variables cannot be accessed outside their function.

#Best practices for global and local variables
#1. Minimize the use of global variables.
#2. Prefer local variables over global ones.
#3. Use parameters and return values instead of relying on global state.
#4. If you must use a global variable, make it clear and well-documented.

#Returning values from functions

#Examples of functions that return values

def square(number):
    return number * number
result = square(5) #store the returned value in a variable
print(result)  # Output: 25

def concatenate_strings(str1, str2):
    return str1 + str2
combined = concatenate_strings("Hello, ", "World!")
print(combined)  # Output: Hello, World!

def calculate_area(length, width):
    area = length * width
    area += 10  # Adding 10 for some reason
    return area


room_area = calculate_area(15, 20)
print(f"The area is {room_area}")  # Output: The area is 150


def double(number):
    return number * 2

#store in variable

total = double(5) + double(20)
print(total)  # Output: 50

if double(10) > 15:
    print("Big Number")  # Output: Big Number

# Returning multiple values from functions

def get_user_info():
    name = "Alice"
    age = 30
    city = "New York"
    return name, age, city  # Returning multiple values as a tuple

user_name, user_age, user_city = get_user_info()
print(user_name)  # Output: Alice

print(user_age)   # Output: 30

print(user_city)  # Output: New York

#Using functions to build a simple program
def calculate_bmi(weight, height):
    """Calculate Body Mass Index (BMI)."""
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Determine BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"
    
def main():
    weight = 170  # in kilograms
    height = 1.75  # in meters
    
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    
    print(f"Your BMI is {bmi:.2f}, which is considered '{category}'.")

main()  # Run the program



