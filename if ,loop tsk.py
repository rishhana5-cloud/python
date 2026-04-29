
#1. Write a program to check whether a number is positive, negative, or zero.

# a=int(input("enter a number"))
# if a==0:
#     print("zero")
# elif a<1:
#     print("negative")
# else:
#     print("positive")

#2. Check if a number is even or odd

# num=int(input("enter a number"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

#3. Given a number, check if it is greater than 100

# a=150
# if a>=100:
#     print("greater than 100")
# else:
#     print("less than 100")

#4. Check whether a person is eligible to vote (age ≥ 18)

# age=8
# if age>=18:
#     print("eligible to vote ")
# else:
#     print("no eligible to vote")

#5. Given two numbers, print the greater number

# a=20
# b=40
# if a>=b :
#     print("20 is greater number")
# else:
#     print("40 is greater number")

#6. Given three numbers, print the largest number
# a=5
# b=10
# c=15
# if a>=b and a>=c:
#     print("a is largest number")
# elif b>=a and b>=c:
#     print("b is largest number")
# else:
#     print("c is largest number")

#7. Check whether a year is a leap year.

# year=int(input("enter a year"))
# if year%400==0:
#     print("leap year")
# elif year%100==0:
#     print("not aleap year")
# elif year%4==0: 
#     print("leap year")
# else:
#     print("not a leap year")

"""8. Given a mark, print:
"Pass" if marks ≥ 40
"Fail" otherwise"""

# mark=30
# if mark>=40:
#     print("Pass")
# else:
#     print("Fail")

"""9. Given a mark, print grades:
A → ≥ 90
B → ≥ 75
C → ≥ 60
Fail → below 60"""

# mark=80
# if mark>=90:
#     print("A")
# elif mark>=75:
#     print("B")
# elif mark>=60:
#     print("C")
# else:
#     print("fail")

#10. Check if a character is a vowel or consonant.

# vowel="AEIOU"
# character="A"
# if character in vowel:
#     print("vowel")
# else:
#     print("consonant")

#11. Print numbers from 1 to 10 but stop when number is 6

# for i in range(1,11):
#     if  i==6:
#      break
#     else:
#      print(i)

#12. Print numbers from 1 to 10 but skip number 5.
# for i in range(1,11):
#     if i==5:
#         continue
#     else:
#         print(i)

#13. Use pass inside an if block and explain why it doesn’t cause an error
# a=10
# if a<=5:
#     pass
# else:
#     print("not")

"there is  doesn't cause an error because future code writing"

"""sometimes you don't want to write code yet.
So instead of leaving it empty (which gives error ), you use:
pass """

#14. Print all even numbers between 1 and 20 
# for i in range(1,21):
#     if i%2==0:
#         print(i)


#15. Find the sum of numbers from 1 to 10.
# sum=0
# for i in range(1,11):
#  sum+=i
# print(sum)

#16. Check whether a given number is a multiple of both 3 and 5
# number=11
# if number%3==0 and number%5==0:
#     print("number is a multiple of both 3 and 5")
# else:
#     print("not multiple of both")

#17. Print "Hello" 5 times using a loop.

# for i in range(5):
#     print("Hello")

#18. Given a list [1,2,3,4,5] , print only numbers greater than 3.
# num=[1,2,3,4,5] 
# for i in num:
#  if i >=3:
#   print(i)


"""Write a Python program to simulate a login system with the following rules:

The correct username is "admin" and the correct password is "1234" 

The user is allowed a maximum of 3 login attempts.

The username comparison should be case-insensitive.

The password comparison should be case-sensitive.

If the user enters correct credentials within the allowed attempts, display
Login successful
 
If all attempts are used without success, display
Account locked 
After each failed attempt, display the number of attempts remaining"""

# username="admin"
# password=1234

# if username=="admin":
#     if password==1234:
#         attempt=3
#         print("login successful")
#     else:
#         print("account locked") 
# else:
#     print("account locked") 


"""20. Enhanced Traffic Light Controller

Write a Python program that acts as a traffic light controller with the following
conditions:

The program should accept either a color or a number as input.

Use the mapping:
1 or "red" → Stop and wait for 60 seconds
2 or "yellow" → Ready and wait for 5 seconds
3 or "green" → Go and drive safely

The program should handle inputs in a case-insensitive manner.
If the input does not match any valid color or number, display
Invalid signal """

# signal=input("enter1/2/3 or red/yellow/green").lower()

# if signal=="red" or signal==1 :
#     print("Stop and wait for 60 seconds")
# elif signal=="yellow"or signal==2 :
#     print("Ready and wait for 5 seconds")
# elif signal=="green"or signal==3 :
#     print("Go and drive safely")
# else:
#     print("Invalid signal")


#LIST COMPREHENSION QUESTIONS

"""1. Given a list of numbers, write a program to find the sum of all numbers, the
sum of even numbers, and the sum of odd numbers using list
comprehension."""



