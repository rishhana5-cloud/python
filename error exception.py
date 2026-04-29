

    #zero division error

# a=15
# b=0
# print(a/b)


    #  type error

# def abc(name):
#     print("5"+5)
# abc("rish")

     #value error

# def bv(st):
#  print(int("rish"))
# bv(12)


     #index error
# a=[1,2,3]
# print(a[3])

 
      #key error
# a={
#     "name":"rish",
#     "age":30,
# }
# print(a["place"])


     #file not found error

# file=open("sptyle.txt","r")
# file.close()



           #Exception Handling with "try-except"----->

# try:
#     a=10/2
#     print(a)
# except ZeroDivisionError:
#     print("you can't devided by zero")
 
        #or
# try:
#     b=10/0
#     print(b)
# except Exception as e:
#     print(e)

# try:
#     file=open("style.txt","r")
# except FileNotFoundError:
#     print("file not found")


           # "else and finally" in Exception Handling----------> 

# try:
    
#   num=int(input("enter a number"))
#   result=10/num
# except ZeroDivisionError:
#   print("division by zero is not allowed")
# else:
#   print(f"result is{result}")
# finally:
#   print("this will always be printed")

               #Raising Exceptions ---------->
# x=5
# if x>0:
#     raise TypeError("positive numbers are not allowed")

              #Custom Exceptions --------------->

# class rishanaError(Exception):
#     pass
# def custom(num):
#     if num<0:
#       raise rishanaError("negative numbers are not allowed")
# try:
#  custom(-10)
# except rishanaError as e:
#    print(e)









