
                 #FILE HANDLING QUESTIONS
"""1. Write a program to create a file named data.txt and write the text
"Hello File Handling" into it"""

# with open("data.txt","w") as file:
#  file.write("Hello File Handling")

"""2. Write a program to read the contents of a file data.txt and display it on the
screen."""

# with open ("data.txt","r")as file:
#  content= file.read()
#  print(content)

"""3. Write a program to append the text "Python is awesome" to an existing file."""
# with open("data.txt","a")as file:
#  content=file.write("Python is awesome\n")
 
"""4. Write a program to count the number of lines present in a file."""
# with open("data.txt","r")as file:
#  content=file.readlines()
#  print(content)

"""5. Write a program to count the number of words in a file."""
# with open("data.txt","r")as file:
#  content=file.read()
#  count=content.split()
 
#  print(len(count))

"""6. Write a program to copy the contents of one file into another file"""
# with open ("data.txt","r")as file:
#    content= file.read()


# with open("sample.txt","w")as fileb:
#     fileb.write(content)
#     print(content)

"""7. Write a program to read a file and print only the lines that contain the word
"Python" """

# with open ("data.txt","r")as file:
#    for i in file:
#      if "python" in i.lower():
#       print(i)

"""8. Write a program that reads numbers from a file and calculates their sum."""
# with open ("data.txt","r")as file:
#     data=file.readlines()
#     total=0
#     for i in data:
#       num=int(i)
#       total+=num
# print(total)

"""ERROR HANDLING (EXCEPTION
HANDLING) QUESTIONS"""

"""9. Write a program to handle a ValueError when the user enters invalid input (for
example, entering letters instead of a number)"""

# try:
#     a=int(input("enter a number"))
#     result= a*2
#     print(result)
# except ValueError:
#     print("you entered invalid input")
        

"""10. Write a program to handle invalid input (user enters a string instead of a
number)."""
# try:
#     a=int(input("enter a number"))
#     print(a)
# except ValueError:
#     print("you entered invalid input")

"""11. Write a program that handles file not found error while opening a file"""
# try:
#  with open("file.txt","r")as file:
#     print("file opened")
# except FileNotFoundError:
#     print("file not found")

"""12. Write a program using try , except , and else blocks."""
# try:
#    result=10/5
# except ZeroDivisionError:
#    print("cannot divided by zero")
# else:
#    print(f"result is {result}")   

"""13. Write a program using try , except , and finally to ensure a message
"Program ended" is always printed."""
# try:
#    result=10/5
# except ZeroDivisionError:
#    print("cannot divided by zero")
# else:
#    print(f"result is {result}")  
# finally:
#    print("program ended")   

"""14. Write a program that catches multiple exceptions using multiple except
blocks."""
# try:
#    a=int(input("enter a number"))
#    result=10/a
# except ZeroDivisionError:
#    print("cannot divided by zero")
# except ValueError:
#    print("invalid input")
# else:
#    print(f"result is {result}")  
# finally:
#    print("program ended")   


"""15. Write a program that raises a custom error when the user enters a negative
number."""
# class negativeNumberError(Exception):
#     pass
# def custom(num):
#     if num<0:
#         raise negativeNumberError("negative numbers are not allowed")

# try: 
#  a=int(input("enter a number"))  
#  custom(a) 
# except negativeNumberError as n:
#    print(n)


"""MODULES & LIBRARIES (BUILT-IN + USERDEFINED)"""

"""🔹 Built-in ( math only)

16. Write a program that uses the math module to find the square root of a
number."""

# import math
# print(math.sqrt(20))

"""17. Write a program that uses the math module to calculate power of a number."""
# import math
# print(math.pow(2,3))

"""18. Write a program that uses the math module to find the factorial of a number."""
# import math
# print(math.factorial(5))

"""🔹 User-Defined Modules

19. Create a user-defined module named calculator.py that contains functions
for addition, subtraction, multiplication, and division.
Import and use this module in another Python file."""

"""20. Create a user-defined module that contains a function to check whether a
number is even or odd, and use it in another program."""


