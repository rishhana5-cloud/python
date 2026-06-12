
# items=[]

# def add_item():
#     add=input("enter item name")
#     items.append(add)
#     print("item added successfully")


# def view_items():
#     if len(items)==0:
#         print("empty")
#     else:
#         for i in items:
#             print(i)


# def remove_item():
#    rmv=input("Enter item name to remove")
#    if rmv in items:
#      items.remove(rmv)
#      print("item removed successfully")

# def exit_item():
#         print("exiting....")

# while True:
#     choice=input("enter your choice:")
#     if choice=="1":
#         add_item()
#     elif choice=="2":
#         view_items()
#     elif choice=="3":
#         remove_item()
#     elif choice=="4":
#         exit_item()
#         break


# def numb():
#  n=5
#  s=[""]
#  for i in range(1,n+1):
#   s.append(i)
#  print(s)
# numb()


# class Employee:
#     def employee_id(self):
#         self.emp_id=input("enter Employee id:")
    
#     def display_employee_id(self):
#       print(f"Employee id:{self.emp_id}")

# class Manager(Employee):
#    def get_department(self):
#       self.department=input("enter DEPARTMENT:")

#    def display_department(self):
#        print(f"DEPARTMENT:{self.department}")


# class SeniorManager(Manager):
#    def get_team_size(self):
#       self.team_size=input("enter team size:")

#    def display_team_size(self):
#       print(f"team size:{self.team_size}")

# sm=SeniorManager()
# sm.employee_id()
# sm.get_department()
# sm.get_team_size()


# class Marks:
#     def mark(self):
#      self.math=int(input("enter sub1 mark:"))
#      self.phy=int(input("enter sub2 mark:"))
#      self.eng=int(input("enter sub3 mark:"))

# class Sports:
#    def sports_score(self):
#       self.sport_score=int(input("enter sports score:"))     


# class Result(Marks,Sports):
#    def display_total_marks(self):
#        total=self.math+self.phy+self.eng
#        return total


#    def Average_result(self):
#        average=self.display_total_marks()/3
#        return average

#    def final_score(self):
#       final=self.display_total_marks()+self.sport_score
#       return final






# arr = [3,1,2,4]
# lst=[]

# for i in arr:
#   if arr%2==0: 
#     print(lst.append(arr))
    
#   else:
#     print(i)


arr = [-10, -10, 5, 2]

def mult():
  for i in arr :
     if arr==[2]:
        break
     return i*i
  
 
  print(i)
  mult()

