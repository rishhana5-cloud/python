

# a={"name":"rish",
#    "age":22,
#    "city":"manjeri"}

# print(a.get("name"))        #it returns None, if the key doesn't exist instead of raising an error
# print(a["name"])

# b=dict( name="rish",
#        age=22,
#        state="kerala")

# b["name"]="riff"
# print(b)

 
           #adding items--------->

# c=dict( name="rish",
#        age=22,
#        state="kerala")

# c["city"]="manjeri"
# print(c)

        #removing items---------->
 
# dict = {"name": "John", 
#            "age": 30, 
#            "city": "New York"}      #it raise an error

# dict.pop("place")
# print(dict)


# dct = {"name": "John", 
#            "age": 30}

# dct.popitem()
# print(dct)


# dict = {"name": "John",
#          "age": 30}

# del dict ["age"]
# print(dict)



# dict = {"name": "John",
#          "age": 30}

# dict.clear()
# print(dict)


# original = {"name": "John",
#              "age": 30}

# cpy=original.copy()
# print(cpy)


# original = {"name": "John",
#              "age": 30}
# cpy_items=dict(original)
# print(cpy_items)

# dict={
#    "person1": {
#        "name":"rish",
#        "age":22},

#     "person2":{
#         "name":"riff",
#         "age":45
#     }
# }
# print(dict["person1"])
# print(dict["person2"])
# print(dict["person2"] ["name"])


s={
    "name":"jish",
    "age":33
}
# print(s.keys())
# print(s.values())
# print(s.items())


# s={
#     "name":"jish",
#     "age":33
# }
# s.update({"city":"manjeri",
#           "state":"kerala"})
# print(s)

# kees=["name","age","city"]
# new_kees=dict.fromkeys(kees,"none")
# print(new_kees)


# my={
#     "name":"sana",
#     "age":44,
#     "place":"narukara"
# }

# your=my.setdefault("place","manjeri")
# print(my)


# my={
#     "name":"sana",
#     "age":44,
# }

# your=my.setdefault("place","manjeri")
# print(my)

