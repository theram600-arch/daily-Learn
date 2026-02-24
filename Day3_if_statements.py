                              # Conditional execution: a block of one or more statements will be executed if a certain expression is true

# If else condition
# In python and other programming languages the key word if is used to check if a condition is true and to execute the block code. Remember the indentation after the colon.

# a = 3
# if a < 0:
#     print('A is a negative number')
# else:
#     print('A is a positive number')

# # elif condtion
# a = 0
# if a > 0:
#     print('A is a positive number')
# elif a < 0:
#     print('A is a negative number')
# else:
#     print('A is zero')

# # Nested if

# a = 0
# if a > 0:
#     if a % 2 == 0:
#         print('A is a positive and even integer')
#     else:
#         print('A is a positive number')
# elif a == 0:
#     print('A is zero')
# else:
#     print('A is a negative number')


# # Positive / Negative / Zero
# num = int(input("Enter number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# # Even or Odd
# num = int(input("Enter number: "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # Voting Eligibility
# age = int(input("Enter age: "))

# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")


# # Grade System
# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")


# # Largest of Two Numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b:
#     print("Largest:", a)
# elif b > a:
#     print("Largest:", b)
# else:
#     print("Both are equal")

# # Simple Calculator
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operator (+,-,*,/): ")

# if op == "+":
#     print(a + b)
# elif op == "-":
#     print(a - b)
# elif op == "*":
#     print(a * b)
# elif op == "/":
#     print(a / b)
# else:
#     print("Invalid operator")



# # Login System
# username = input("Enter username: ")

# if username == "admin":
#     password = input("Enter password: ")
#     if password == "1234":
#         print("Login Successful")
#     else:
#         print("Wrong Password")
# else:
#     print("User not found")
# # Number Check (Nested)
# num = int(input("Enter number: "))

# if num > 0:
#     if num % 2 == 0:
#         print("Positive Even")
#     else:
#         print("Positive Odd")
# else:
#     print("Negative number")
# # Scholarship Eligibility
# marks = int(input("Enter marks: "))
# income = int(input("Enter income: "))

# if marks >= 80:
#     if income < 300000:
#         print("Eligible for scholarship")
#     else:
#         print("Not eligible due to income")
# else:
#     print("Not eligible due to marks")




# username=input("enter your name: ")

# if len(username)>12:
#     print("letters are more than 12, your can print")
# elif not username.find(" ")==-1:
#     print("your username cannot contain spaces")
# elif not username.isalpha():
#     print("your usename cannot contain numbers")

# else:
#     print(f"welcome, {username}")