# class Person:
#     def __init__(self,name,height,weight):
#         self.name=name
#         self.height=height  
#         self.weight=weight
       
     
#     def display(self):
#         print(f"this is{self.name}with{self.height}height and weight is {self.weight}") 

# person1=Person("rishana",150,65)
# person2=Person("susmi",100,20)
# print(person1.height)
# print(person2.name)

# person1.weight=70
# person1.display()
# person2.display()


                           #__str__() Method


# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author

#     def __str__(self):
#         return f"'{self.title}'by {self.author}"

# book=Book("1984","rishana")
# print(book)


                      # Class Variables vs Instance Variables

# class Employee:
#     companay="sofcroniics"

#     def __init__(self,name,position):
#         self.name=name
#         self.position=position

# emp1=Employee("john","mamager")
# emp2=Employee("Alice","developer")

#              #accessing class variable------>

# print(emp1.name)
# print(emp2.name)

#             #accessing instance variable----->

# print(emp1.companay)
# print(emp2.companay)


                 #inner class and outer class--------->

# class Employee:
#     class company:
#         def __init__(self,cname,location):
#          self.cname=cname
#          self.location=location

#     def __init__(self,employeename,salary,cname,location):
#          self.employeename=employeename
#          self.salary=salary
#          self.company=Employee.company(cname,location)

    # def display(self):
    #     print(f"name:{self.employeename},salary:{self.salary} company:{self.company.cname} location:{self.company.location}")

        
# emp=Employee("rishana","50,0000","xyz crop","london")
# emp.display()
# print(emp.company.location)

                #Tightly Coupled Composition---------->



# class Company:
#     def __init__(self,cname,location):
#         self.cname=cname
#         self.location=location

# class Employee:
#     def __init__(self,empname,salary,cname,location):
#         self.empname=empname
#         self.salary=salary
#         self.Company=Company(cname,location)

# emp=Employee("devu",50000,"abc company","london")
# print(emp.empname)       




# class Company:
#     def __init__(self,cname,location):
#         self.cname=cname
#         self.location=location

# class Employee:
#     def __init__(self,empname,salary,Cmp):
#         self.empname=empname
#         self.salary=salary
#         self.Cmp=Cmp

#     def display(self):
#         print(f"name:{self.empname},salary:{self.salary} company:{self.Cmp.cname} location:{self.Cmp.location}")

# c=Company("abc company","london")
# emp=Employee("devu",50000,c)
# emp.display()

          #oop-task--------------------------->

# class Student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
    
#     def display_grade(self):
    
#         if self.mark >=90:
#             print("Grade:A")
#         elif self.mark>= 75 and self.mark <90:
#          print("Grade:B")
#         elif self.mark>=50 and self.mark<75:
#          print("Grade:C")
#         else:
#          print("fail")
#         print(f"name:{self.name},mark:{self.mark}")
        
# m=Student("rish",90)  
# m.display_grade()


# class Student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark

#     def calculate_average(self):

#      return sum(self.mark)/len(self.mark)
    
#     def display_grade(self):
    
#         average=self.calculate_average

#         if average >=90:
#             print("Grade:A")
#         elif average>= 75 and average <90:
#          print("Grade:B")
#         elif average>=50 and average<75:
#          print("Grade:C")
#         else:
#          print("fail")
#         print(f"name:{self.name},mark:{self.mark}")
        
# m=Student("rish",{"math":60})  
# m.display_grade()

              #Encapsulation------>

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name               #public attribute
#         self.__salary= salary          #private attribute

#     def display__employee(self):
#         print(f"name:{self.name},salary:{self.__salary}")

#     def update__salary(self,new_salary):
#      self.__salary=new_salary

# emp=Employee("rish",50000)
# # emp.display__employee
# emp.update__salary(30000)
# emp.display__employee()

     #TASK----------------------------
# class BankAccout:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance

#     def deposite(self,amount):
#         self.amount=amount
#         if amount>0:
#             return sum(self.amount)+self.__balance 

#     def withdraw(self):
#         if self.amount>0 and self.__balance<self.amount:
#              return self.withdraw


#     def get_balance(self):
#        self.deposite-self.withdraw

# bank=("Alice,1000")
# bank.deposite=(500) 
# withdraw=(200)
# print(BankAccout.get_balance)

            #INHERITANCE-------------->
               #single inheritance

# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):    
#         print(f"{self.name}make a sound")
   
# class Dog(Animal):
    #pass 

    # def __init__(self,name):
    #     self.name=name


    # def speak(self):
    #     print(f"{self.name}says woof!")


# dog=Dog("buddy")
# dog.speak()

         #MULTIPLE INHERITANCE------>

# class Engine:
#     def start_engine(self):
#         print("Engine started")

# class Wheels:
#     def rotate(self):
#         print("wheels are rotating")

# class Car(Engine,Wheels):
#     def drive(self):
#         print("car is driving")

# car=Car()
# car.start_engine()
# car.rotate()
# car.drive()

           #Multilevel Inheritance---->

# class Grandparent:
#     def sing(self):
#         print("grandparent is singing")

# class Parent(Grandparent):
#     def dance(self):
#         print("parent is dancing") 

# class Child(Parent):
#     def play(self):
#         print("child is playing")      

# child=Child()
# child.sing()
# child.dance()
# child.play()

          #Hierarchical Inheritance----->

# class Animal:
#   def speak(self):
#     print("Animal speaks")

# class Dog(Animal):
#   def speak(self):
#     print("Dog barks")    

# class Cat(Animal):
#   def speak(self):
#     print("cat meows")

# dog=Dog()
# cat=Cat()

# dog.speak()
# cat.speak() 

          #Hybrid Inheritance----->

# class A:
#     def method_a(self):
#         print("method from A")

# class B(A):
#     def method_b(self):
#         print("method from B")        

# class C(A):
#     def method_c(self):
#         print("method from c")

# class D(B,C):
#     def method_d(self):
#         print("method from d")

# d=D()
# d.method_a()
# d.method_b()
# d.method_c()
# d.method_d()

          #Polymorphism----------->

# class Animal:
#     def speak(self):
#         return "some sound"
    
# class Dog(Animal):
#     def speak(self):
#         return "whoof"    

# class Cat(Animal):
#     def speak(self):
#         return "meow"
    
# animal=[Dog(),Cat()]
# for a in animal:
#     print(a.speak())

        #Method Overriding------>


# class Animal:
#     def speak(self):
#         print("animal makes a sound")

# class Dog(Animal):
#     def speak(self):
#         print("dog says whoof!")

# class Cat(Animal):
#     def speak(self):
#         print("cat says meow")

# animal=[Dog(),Cat()]
# for i in animal:
#     i.speak() 


        #Duck Typing---->

# class Dog:
#     def speak(self):
#         print("whoof")

# class Cat:
#     def speak(self):
#         print("meow")

# class Human:
#     def speak(Animal):
#         print("hello")

# animal=[Dog(),Cat()]
# for i in animal:
#     i.speak() 

                # Abstraction------->

# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#        pass

# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height


#     def area(self):
#         return self.width*self.height


# rectangle=Rectangle(10,20)
# print(rectangle.area())


        #Constructor and Destructor--------->

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"{self.name} has been created")


#     def __del__(self):
#         print(f"{self.name} has been destroyed")

# p1=Person("rish",10)
# del p1


          #DECORATOR-------->
          #Without argument

# def chocolate(sweet):
#   def candle():
#      print("cake ready")
#      sweet()
#      print("cake finish")
#   return candle

# @chocolate
# def cake():
#     print("icecream")

# cake()

     #with argument-------------->
# def chocolate(sweet):
#   def candle():
#      print("cake ready")
#      sweet()
#      print("cake finish")
#   return candle

# @chocolate
# def cake(name):
#     print("cake")

# cake()

           # Class Methods-------->
# class Company:
#     companyname="techcompany"

#     @classmethod
#     def change_name(cls,new_name):
#      cls.companyname=new_name

              # Change class variable through a class method-----------

# Company.change_name("future solution")
# print(Company.companyname)



                  #Static Methods-------

# class Mathoperators:

#     @staticmethod
#     def add(a,b):
#         return a+b

# abcd=Mathoperators()             #object
# print(abcd.add(2,2))



nums=(10,20,30)
nums.__iter__()
print(nums)
