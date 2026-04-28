     #creating list--------------->

# a=["hello",12,1.4,"by","by","by"]
# print(a)

# a=["banana","apple","orange"]
# print(a[-1])

# a=[10,20,30,40,50]
# print(a[1:4])

# a=["banana","apple","orange"]
# a[1]="mango"
# print(a)

# a=["banana","apple","orange","mango"]
# a[1:2]="a","b"
# print(a)

            #adding items------->

# a=["banana","apple","orange","mango"]         #last add any element use append
# a.append("cherry")
# print(a)

# a=["banana","apple","orange","mango"] 
# a.insert(3,"strawberry")                        
# print(a)

# a=["apple","orange"]
# b=["banana","pappaya"]
# b=a.extend(b)
# print(a)

           #removing items for a list

# a=['apple', 'orange', 'banana', 'pappaya']
# a.remove("orange")
# print(a)

# a=['apple', 'orange', 'banana']
# b=a.pop()
# print(a)                                 #returning value


# a=['apple', 'orange', 'banana', 'pappaya']     
# del a[]                                            #dlt full list
# print(a)

# a=['apple', 'orange', 'banana', 'pappaya']          #clear only list items
# a.clear()
# print(a)


         #List Comprehensions ----------------->
# a=[]
# for i in range(1,10) :
#    a.append(i)
# print(a)

# a=[i for i in range (1,11)]
# print(a)

# a=[i**2 for i in range (1,11)]
# print(a)

# a=[i**2 for i in range (1,11) if (i%2==0)]
# print(a)


          #list method------------------>

# a=[1,2,3,4,1]
# print(a.index(4))

# a=[1,2,3,4,1]
# print(a.count(1))

# a=[1,2,3,4,1]
# b=a.reverse()
# print(a)

# a=[1,3,2,4,]
# a.sort(reverse=True)
# print(a)

# a=[1,2,3,4,1]
# b=a.copy()
# print(a)

# a=[1,2,3,4,1,3]               #no change og list only change sorted list
# b=sorted(a)
# print(b)


# a=[1,2,3,4,1]
# b=a[:]
# print(b)

# a=[1,2,3,4]
# b=[5,6,7,8]
# c=a+b
# print(c)

# a=["orange","apple"]
# b=["banana","pappaya"]
# b=a.extend(a)  
# a.extend(b)
# print(a)







