
# a=set([1,2,3,4,5])
# print(a)

# a={1,2,3,4,5}
# print(4 in a)
# print(10 in a)
                                
                                  #add

# items={"apple","orange","pappaya"}
# items.add("kivi")                                  add    #add one item ()
# print(items)

# item={"apple","banana"}                           update      #adding multiple item ([])
# item.update(["orange","grapes"])
# print(item)


                                     #remove

# items={1,2,3,4,5}
# items.remove("orange")                   #raises a key error
# print(items)


# items={1,2,3,4,5}
# items.discard(8)                          #not raise an error
# print(items)


# items={1,2,3,4,5}
# move=items.pop()
# print(move)

# it={1,2,3,4,5}
# it.clear()
# print(it)



                    #joining sets

# a={1,2,3,3,3}                       
# b={4,5,6}               #==union   duplicates removed
# new=a.union(b)
# print(new)

# a={1,2,3,3,3}                       
# b={4,5,6} 
# a.update(b) 
# print(a)

               #set intersection (&)

# s={1,2,3}
# i={2,3,4}
# result=s&i              #return common elements
# print(result)


           #-------------------
            #set difference (-)
# s={1,2,3}
# i={2,3,4}                  #present in the 1st set                                                
# result=s-i                 #not in the second set
# print(result)

                         
        #set symmertric difference (^)

# set1={1,2,3}
# set2={2,3,4}
# result=set1 ^ set2      different elements in 2 set
# print(result)

# set1={1,2,3}
# set2={1,2,3,4,5}                 #sub set
# print(set1.issubset(set2))


# set1={1,2,3}
# set2={1,2,3,4,5}                    #super set
# print(set2.issuperset(set1))       #set2 contains all elements of set1
                                    #so,set2 is super set


# frz=frozenset([1,2,3,4,5])
# print(frz)














