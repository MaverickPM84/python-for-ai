#Data Structures in Python, help in storing multiple values in a single variable

#Think of data structures as containers that can hold and organize multiple pieces of data.
#They allow us to group related data together and perform operations on them efficiently.

#Lists - like a shopping list ( ordered items) 
# lists can be used to store a collection of items, such as numbers, strings, or even other lists. 
# They are ordered, meaning that the items have a specific order and can be accessed using their index. 
# Lists are mutable, which means that you can change their contents after they have been created.
#lists - Ordered changeable collection of items, allows duplicate values. 
#Lists are defined using square brackets [] and can contain any type of data, including other lists.

shopping_list = ["milk", "eggs", "bread", "fruits"]
print(shopping_list)  # Output: ['milk', 'eggs', 'bread', 'fruits']

need_everyday = shopping_list[0]
print(need_everyday)  # Output: milk , get first item in the list

need_sometimes = shopping_list[-1]
print(need_sometimes)  # Output: fruits, get last item in the list

#changing list item
shopping_list[1] = "butter"
print(shopping_list)  # Output: ['milk', 'butter', 'bread', 'fruits']

shopping_list.append("vegetables")
print(shopping_list)  # Output: ['milk', 'butter', 'bread', 'fruits', 'vegetables']

#list insert item at specific position
shopping_list.insert(2, "eggs")
print(shopping_list)  # Output: ['milk', 'butter', 'eggs', 'bread', 'fruits', 'vegetables']

shopping_list.remove("bread")
print(shopping_list)  # Output: ['milk', 'butter', 'eggs', 'fruits', 'vegetables']

#del keyword to remove item at specific index
del shopping_list[0]
print(shopping_list)  # Output: ['butter', 'eggs', 'fruits', 'vegetables']

#list methods
print(len(shopping_list))  # Output: 4, get number of items in the

#list count method
print(shopping_list.count("eggs"))  # Output: 1, count occurrences of "eggs"

#index method
print(shopping_list.index("fruits"))  # Output: 2, get index of "fruits"

#sorting a list
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]

#reversing a list
numbers.reverse()
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]

#Copying a list
new_list = shopping_list.copy()

print(new_list)  # Output: ['butter', 'eggs', 'fruits', 'vegetables']

#Checking lists




#Dictionaries - like a phone book (name > number)
#Dictionaries - Unordered, changeable collection of key-value pairs, no duplicate keys allowed. USed for fast lookups based on keys.
#Dictionaries are defined using curly braces {} and consist of key-value pairs, where each key is unique and maps to a corresponding value.

phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}

print(phone_book)  # Output: {'Alice': '123-456-7890', 'Bob': '987-654-3210', 'Charlie': '555-555-5555'}

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

person["age"]
person["city"] = "San Francisco"
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'San Francisco'}

# aDD TO dictionary
person["profession"] = "Engineer"

del person["age"]
print(person)  # Output: {'name': 'Alice', 'city': 'San Francisco', 'profession': 'Engineer'}

#dictionary methods
print(len(person))  # Output: 3, get number of key-value pairs

print(person.keys())  # Output: dict_keys(['name', 'city', 'profession']), get all keys

print(person.values())  # Output: dict_values(['Alice', 'San Francisco', 'Engineer']), get all values




#Tuples - like coordinates (fixed values)
#Tuples - Ordered, unchangeable collection of items, allows duplicate values
#Tuples are like lists, but they can't be changed once created

#Use tuples for data that should not be modified, such as coordinates or fixed settings.
#Tuples are defined using parentheses () and can contain any type of data.
# Coordinates of a point in 3D space
# RGB color values
#Database records that should remain constant
#Function return values that should not be altered




coordinates = (10, 20, 30)
print(coordinates)  # Output: (10, 20, 30)

coordinates[0] = 15  # This will raise a TypeError, as tuples are immutable


#Accessing tuple items

print(coordinates[0])  # Output: 10, get first item in the tuple

#slicing a tuple
print(coordinates[1:])  # Output: (20, 30), get items from index 1 to the end

print(coordinates[0:2])  # Output: (10, 20), get items from index 0 to index 1


#Sets - like a bag of unique items (unordered)
#Sets - Unordered collection of unique items, no duplicate values allowed
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

fruits = set(["apple", "banana", "cherry"])
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

empty_set = set()
print(empty_set)  # Output: set()

# From a list (removing duplicates)
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers_from_list = set(numbers_list)
print(unique_numbers_from_list)  # Output: {1, 2, 3, 4, 5}

