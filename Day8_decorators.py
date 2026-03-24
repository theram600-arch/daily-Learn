
# '''These decorator functions are higher order functions
# that take functions as parameters'''

# # First Decorator
# def uppercase_decorator(function):
#     def wrapper():
#         print("hello there")
#         return function()
        
    
#     return wrapper

# # Second decorator
# def split_string_decorator(function):
#     def wrapper():
#         print("ram")
#         return function()
       
        
#     return wrapper


# #Decorators will be executed from bottom to top
# @uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
# @split_string_decorator
# def greeting():
#     return "Welcome to Python"

# print(greeting())   # ['WELCOME', 'TO', 'PYTHON']





