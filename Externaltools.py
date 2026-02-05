#External tools for Python for AI

#extend python with packages and libraries

#What are packages and libraries?
#Packages and libraries are collections of pre-written code that provide additional functionality to Python.
# They allow you to extend Python's capabilities without having to write everything from scratch.

#Packages are just python files containing code, typically combinations of functions & classes.
#Libraries are collections of packages that provide specific functionality.
#When you import a package, you're bringing that functionality into your own code.

#Python's ecosystem

#Python has a vast ecosystem of packages and libraries for various purposes, including:

#Data Manipulation - pandas, numpy
#Machine Learning - scikit-learn, TensorFlow, PyTorch
#Data Visualization - matplotlib, seaborn
#Web Development - Django, Flask
#Natural Language Processing - NLTK, spaCy
#Web Scraping - Extract data from websites using BeautifulSoup, Scrapy
#Data Analysis - Perform data analysis and manipulation using pandas, numpy
#Machine Learning - Build and train machine learning models using scikit-learn, TensorFlow, PyTorch
#APIs - Interact with web services and APIs using requests, httpx, connect to online services and retrieve data.
#Automation - Automate repetitive tasks using libraries like selenium, pyautogui

#Import Packages

# 2 types of packages

#Built-in - Standard Library - Built-in packages that come with Python installation.
#External - Third-Party Libraries - Packages developed by the community that can be installed via package managers like pip.

#Understanding the terminology

#Module - A single Python file containing code (functions, classes, variables) , like math.py
#Package - A collection of modules organized in a directory structure, like numpy
#Library - A collection of packages that provide specific functionality, like TensorFlow
#Framework - A larger structure that provides a foundation for building applications, like Django
#Class - A blueprint for creating objects that encapsulate data and behavior, used in Object-Oriented Programming.
#Function - A reusable block of code that performs a specific task, defined using the def keyword.

#Mental Model

# A functional is like a specific tool (hammer, screwdriver) in a toolbox.
# A module is like a toolbox containing related tools.
# A package is like garage with toolboxes.
# A class is like a blueprint for building tools.
# A library is like a collection of garages with various tools for different purposes.

#Import Patterns

# Pattern 1 - Import the whole module

import math # here you import the entire toolbox

# Now use math.sqrt(16)

math.sqrt(16)

# Pattern 2 - Import specific items from a module

from math import sqrt, pi # here you import specific tools like sqrt & pi from the toolbox 'math'

result = sqrt(16) * pi
print(result)


import random

# use module functions

number = random.randint(1,10)
print(number)
choice = random.choice(["apple", "banana", "mango"])

print(choice)


# Date and Time

import datetime

today = datetime.date.today()
print(today)


#Operating system

import os
current_dir = os.getcwd()
print(current_dir)

#import JSON

import json

data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)

#import with alias

import pandas as pd

df = pd.DataFrame(data)

#Installing packages




