height = float(input("Enter your height in centimeters: "))

weight = float(input("Enter your weight in kilograms: "))

bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}, you are underweight.")
elif 18.5 <= bmi < 24.9:
    print(f"Your BMI is {bmi:.2f}, you have a normal weight.")
elif bmi >= 25:
    print(f"Your BMI is {bmi:.2f}, you are overweight.")



# Example of if-elif-else to determine status code description

status_code = int(input('Status Code: '))
if status_code == 400:
    description = 'Bad Request'
elif status_code == 401:
    description = 'Unauthorized'
elif status_code == 403:
    description = 'Forbidden'
elif status_code == 404:
    description = 'Not Found'
elif status_code == 405:
    description = 'Method Not Allowed'
elif status_code == 418:
    description = 'I am a teapot'
elif status_code == 429:
    description = 'Too many requests'
else:
    description = 'Unknown status Code'
print('Status Code:', description)

# same code with match case

status_code = int(input('Status Code: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown status Code'
print('Status Code:', description)

#Note : The statement with _wildcards caseacts as a wildcard in the code. 
# If no preceding branch matches, the code will proceed to the next branch case _. case _The wildcard option is optional; not every branch structure requires it. 
# If it appears in a branch case _, it can only be placed at the end of the branch structure. 
# If other branches follow it, those branches will be unreachable.

x = float(input("Enter a number: "))

if x > 1:
    y = 3 * x - 5
elif -1 <= x <= 1:
    y = x + 2
else:
    y = 5 * x + 3

print(f"The result is y = {y}")

# Example of grading system using if-elif-else, converting score to grade

score = int(input("Enter your score (0-100): "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif score < 0 or score > 100:
    grade = 'Invalid score'
else:
    grade = 'F'

print(f"Your grade is {grade}")