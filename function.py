
# def hello ():
#     print("how are you")

# hello()


# def hi (name, age):
#  print(f'my name is {name} my age is {age}')

# hi("rishana",20)
# hi("divya",5)


         #types of arguments

# def hello (name, age):
#  print(f'my name is {name} my age is {age}')       #positional argument

# hello("jish",25)


# def key (name,age):
#  print(f'my name is {name} my age is {age}')        #keyword argument
# key(age=25,name="ani")


# def  fault(name="guest"):
#     print(f'my name is {name}')            #default argument

# fault()
# fault("vish")

             #arbitrary and keyword arguments
 
      #arbitrary

# def hello(*arbtry):
#     print(arbtry)
# hello(1,2,3,4,5)
          
#           #keyword argument
# def hi(**kwrd):
#     print(kwrd)
# hi(name="rish",place="kottayam",state="kerala")


#         #args and kwargs in together

# def together(a,*sngl,**kwrd):
#     print(kwrd)
#     print(sngl)
#     print(a)
# together(1,2,3,name="rish",place="kottayam",state="kerala")


# def add (a,b):
#     print(a+b)
# add(2,2)


# def add (a,b):
#     return a+b
# c=add(2,3)
# print(c)


# def doct(a,b):
#     """add two numbers"""         #add documentation in your function
#     return a+b
# print(doct.__doc__)


                                   #lambda

# lm=lambda a,b:a+b
# print(lm(1,2))

                #map,filter,reduce

# numbers=[1,2,3,4,5]
# mp=map(lambda x:x**2,numbers)
# print(list(mp))

# numbers=[1,2,3,4,5,6,7,8,9,10]
# flt=filter(lambda x:x%2==1,numbers)
# print(list(flt))



# from functools import reduce
# numbers=[1,2,3,4,5]
# rd= reduce(lambda x,y:x+y,numbers,0)
# print(rd)


          #higher order function

# def mult (a,b,operator):
#     return operator(a,b)

# add=lambda a,b:a+b
# n=lambda a,b:a-b

# print(mult(2,3,add))
# print(mult(5,2,n))


              #function scope------
       #-----------------------------------

# x=5              #global scope----------<
# def ab():
#     x=10             #local scope---------< without local global will take
#     print(x)

# ab()

# x=4                  #global scope---<
# def abc ():
#     x=3               #enclosing scope-----parent
#     print(x)
#     def abcd():
#                     #local scope-------child
#         print(x)

#     abcd()
# abc()


# def bc(*a):
#     total=0
#     for number in a:
#        total+=number
#     return total
# result=bc(1,2,3,4,5,6,88,99)
# print(result)


           #recursion function------------>

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#        return n*fact(n-1)
# print(fact(5))

# n=5
# result=1
# for i in range(1,n+1):
#    result=result*i
# print(result)


            #tail recursion

# def tail(n,accumulator=1):
#     if n==1 or n==0:
#         return accumulator
#     else:
#         return tail(n-1,accumulator*n)
# print(tail(5))
        

                   #recursive fuction for fibanocci sequences------------>

# def fac(a):
#     if a==0:
#         return 0
#     elif a==1:
#        return 1
#     else:
#         return fac(a-1)+ fac(a-2)

# print(fac(7))

                          #recursive function for sum---------------->

# def sum_list(lst):
#     if not lst:
#         return 0
#     else:
#         return lst[0]+sum_list(lst[1:])
# print(sum_list([1,2,3,4,5]))    


















































