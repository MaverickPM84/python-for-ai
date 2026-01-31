#Datatypes in Python

#Numbers

# 2 types of numbers: Integers and Floating-point numbers

int_num = 10  # Integer, can also be negative or zero.

float_num = 10.5  # Floating-point number

#Basic math operations:

# Addition and Subtraction

sum_result = int_num + float_num  # 10 + 10.5 = 20.5
diff_result = float_num - int_num  # 10.5 - 10 = 0.5

# Multiplication and Division
prod_result = int_num * 2  # 10 * 2 = 20
div_result = float_num / 2  # 10.5 / 2 = 5.25

# Modulus (Remainder)
mod_result = int_num % 3  # 10 % 3 = 1

# Exponentiation / Powers 

exp_result = 2 ** 3  # 2 raised to the power of 3 = 8

# Order of Operations follows PEMDAS/BODMAS rules:

complex_calc = (int_num + float_num) * 2 / (3 - 1)  # ((10 + 10.5) * 2) / (2) = 20.5

# Strings - Working with text data in Python

# be consistent with single or double quotes

# String Operations

string = "My Name is Preetam Kale."  # Double quotes

my_long_string = '''This is a long string that spans multiple lines.
You can use triple single quotes or triple double quotes.'''  # Triple quotes for multi-line strings

first_name = 'Preetam'  # Single quotes
last_name = "Kale"  # Double quotes
full_name = first_name +  " " + last_name

long_dash = "-" * 20  # Repeats the dash character 10 times
print(full_name)
print(long_dash)

#length of string

len(long_dash)

len(full_name)

# Accessing characters in a string (indexing starts at 0)
first_char = full_name[0]  # 'P'
fifth_char = full_name[4]  # 't'
