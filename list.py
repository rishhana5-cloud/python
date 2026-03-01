     #creating list--------------->

# a=["hello",12,1.4,"by"]
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

# a=["banana","apple","orange","mango"]         #last add any variable use append
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


a=[]
for i in range(1,10) :
   a.append(i)
print(a)

