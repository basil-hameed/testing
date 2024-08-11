# Writing my first python code
# print("Hello World!")

# print("My Python Learners")

""" 
Now learning python programming,
Started with python print statement
This is a multiline comments
"""

'''
This is also
a
multiline 
comments
'''

# name = "guvi"
# print(name)

# name = "geeks"
# print(name)


# mytext = "Guvi Geeks Networks"
# print(mytext)

# print(len(mytext))


# myvalue = "Guvi Geeks Private Limited"
# print(variable_name[start_index: end_index: step])
# print(myvalue[2:5]) # 2, 3, 4
# print(myvalue[2:8]) # 2, 3, 4, 5, 6, 7
# print(myvalue[2:12]) # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# print(myvalue[:])
# print(myvalue[2:])
# print(myvalue[:5])
# print(myvalue[-5:-2]) # -5, -4, -3
# print(myvalue[-8:-2]) # -8, -7, -6, -5, -4, -3
# print(myvalue[::-1]) # reversing a string

"""
Palindrome Program

A word read from left to right and right to left remains the same
i.e., madam, malayalam

Write a program to find the given string is palindrome or not
"""

# user_input = "madam"

# reversed_string = user_input[::-1]
# print(reversed_string)

# if user_input == reversed_string: # "madam" == "madam"
#     print("Palindrome") # Indentation through single tab, or use four space bars
# else:
#     print("Not Palindrome")

x = 1 # integer
y = 5.9 # float
z = 8j # complex

# print(type(x))
# print(type(y))
# print(type(z))

# # converted integer into float data type
# a = float(x)
# print(type(a))

# # convert float to integer
# b = int(y)
# print(type(b))

# # convert integer to complex
# c = complex(x)
# print(type(c))

# x = int(1)
# y = float(1)
# z = complex(1)

# print(x)
# print(y)
# print(z)

# #Output
# 1
# 1.0
# (1+0j)


# a = 5
# b = 3
# print(a + b) # addition operator
# print(a * b) # multiplication operator
# print(a / b) # division operator
# print(a - b) # subtraction operator
# print(a % b) # modulus operator ==> remainder
# print(a ** b) # exponential operator ==>5^3 == 125
# print(a // b) # floor division operator ==> Do same operation like division but returns without decimal values

# x = 10
# if  x < 15 and x > 15:
#     print("Yes")
# else:
#     print("No")

# if  x < 15 or x > 15:
#     print("Yes")
# else:
#     print("No")

# if not(x < 15 or x > 15):
#     print("Yes")
# else:
#     print("No")

# x = ["banana", "apple", "cherry", "strawberry"]
# y = "strawberry"

# # print(y in x)
# print(y not in x)

# print(6 & 3)
# """
# 6 =>000000000000000000000110
# 3 =>000000000000000000000011

# 2 =>000000000000000000000010
# """

# x = 500
# y = 500
# if x > y:
#     print(f"{x} is greater")

# elif x == y:
#     print(f"{x} is equal to {y}")

# else:
#     print(f"{y} is greater")


mytext = "My python learners"

# for i in mytext: # i = "M", i = "y" , i = " "
    # print(i)

# myname = "GuviGeeks"

# for char in myname:
#     print(char)

# i = 1
# while i < 6:
#     print(i)
#     i += 1 # i = i + 1 = 1+1 = 2

# mystring = "Python Learners"

# # get the total length of string
# print(len(mystring)) # 15


# mylist = ["apple", "banana", "mango"]
# print(len(mylist))

# # string modification
# mystring = "      Guvi Geeks      "
# # It returns the string in upper case
# print(mystring.upper()) 
# # output "GUVI GEEKS"

# # It returns the string in lower case
# print(mystring.lower())
# # output guvi geeks

# # It returns the string by stripping the empty space before and after the strings
# print(mystring.strip())
# # output Guvi Geeks

# # It splits the string into substrings
# mystring1 = "Guvi. Geeks. Python"
# print(len(mystring1)) # 19

# new_list = mystring1.split(".")
# print(len(new_list)) # 3

# # It replace the character in the string
# mytext = "Hello World!"
# print(mytext.replace("l", "e"))
# # output Heeeo Wored!

# x = "Hello"
# y  = "World"
# a = 5
# b = 8
# print(x + y) # HelloWorld
# print(a + b) # 13

# print(x + " " + y) # Hello World
# print(x, y) # Hello World

# print(x + b)

# # Using F-Format Strings, After python 3.6 Version, they included this.
# name = "John"
# age = 48

# # concatenating name with age of different datatype
# print(f"Name is {name} and age is {age}")

# # also performs operations inside f-strings
# print(f"Name is {name} and my age next year will be {age + 1}")


# name = "Ravi"
# age = 32
# height = 4.5

# print(f"His name is {name}, his age is {age} and his height is {height}")
# print(type(name))
# print(type(age))
# print(type(height))

"""
Write a python program, to check the given number is positive or negative
Input: number - int
Logic: Positive - num > 0, Negative - num < 0 and Zero - num == 0
Output: print(positive or negative)
"""

# assigned variable 
# num = 0

# get user input
# num = int(input())

# # use if statement to check the condition num > 0
# if num > 0:
#     print(f" {num} is Positive")
# # if condition returns false, then it enters into elif block
# elif num == 0:
#     print(f" {num} is Zero")
# # if both conditions returns false, then it enters into else block
# else:
#     print(f" {num} is Negative")


"""
Write a python program to check the given number is odd or even
Input: integer data type
Logic: num % 2 == 0 => Even 
Output: print(odd or even)
"""

# num = int(input())

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")

# # user_input = str(input())
# user_input = float(input())

# print(type(user_input))

# Loops in python - For & While Loop
# for loop
# myfruits = ["apple", "banana", "orange", "strawberry"]

# for fruit in myfruits: # apple, banana...
    # print(fruit)

# for char in "guvi geeks learners":
#     print(char)


# mycountries = ("london", "italy", "sweden")

# for country in mycountries:
#     print(country)

# mystring = "sharing is caring"

# # using break statement with for loop
# for char in mystring:
#     # print(char)
#     if char == "s":
#         break
    
# Output s h a r i n g   i s  c
# using break statement with while loop
# i = 1 
# while i < 100:
#     print(i)
#     if i == 100:
#         break
#     i += 1 # i = i + 1 

# for i in range(20):    
#     if i % 2 != 0:
#         continue
#     print(i)

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)

# for char in range(12):
#     pass

# for x in range(1, 30, 4):
#     if x == 17:
#         break
#     print(x)

# adj = ["red", "big", "taste"]
# fruits = ["apple", "banana", "mango"]

# # Outer loop
# for x in adj:
#     # Inner loop
#     for y in range(4):
#         print(x, y)

# Nested loop example for creating multiplication table
for i in range(2, 4):
    for j in range(1, 11):
        print(i, '*', j, "=", i * j )
    print() # it adds a space after ending the first set of iteration


