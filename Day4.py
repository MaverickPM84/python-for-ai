


#Logical Operators

#These combine boolean values and conditions

age = 25
has_license = True
drunk = False

# AND - both must be true
can_drive = age >= 18 and has_license == True and drunk == True

print(can_drive)

# OR - at least one must be true

day = "Saturday"

is_weekend = (day == "Saturday") or (day == "Sunday")
print("Is weekend:", is_weekend)

# NOT -reverses the boolean value

is_adult = age >= 18
is_minor = not is_adult
print(is_minor)

#Truth Tables
 
# AND: Both must be True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

# OR: At least one must be True  
print(True or False)    # True
print(False or False)   # False

# NOT: Flips the value
print(not True)         # False
print(not False)        # True

#Assignment shortcuts

#Insead of

score = score + 10

#Write

score += 10  # Adds 10 to score

#Wroks with all operators

x = 10
x += 5   # x = x + 5
x *= 20  # x = x * 20
x -= 15  # x = x - 15
x /= 5   # x = x / 5

# Regular division returns float
result = 10 / 2    # 5.0 (not 5)

# Integer division
result = 10 // 2   # 5


#Confusing

# = assigns a value

# == compares values for equality



#booleans

is_logged_in = True
has_premium_account = False
print("Is user logged in?", is_logged_in)

#True needs to be capital T
#False needs to be capital F

#Comparison operators

age = 25

#Equality

print(age == 25)

print(age != 30)

#Greater than and Less than

print(age < 18)
print(age < 30)

print(age >= 25)

print(age <=25)



# Wrong
is_ready = true   # NameError!
is_done = TRUE    # NameError!

# Right
is_ready = True
is_done = False

