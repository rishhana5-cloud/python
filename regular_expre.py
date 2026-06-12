
           #search

# import re
# text="hello world"
# print(re.search(r"world",text))

         #match

# text="hello world"                   #Checks only at the beginning of the string
# print(re.match(r"hello",text))

# print(re.match(r"world", text))  
# None → "world" not at start

        #findall

# text="I have 2 apples and 5 oranges."
# print(re.findall(r"\d+",text))    

# text="I have 23 apples and 55 oranges."    #d gives separate value 
# print(re.findall(r"\d",text))             #\d+ gives group value

          #finditer

# text = "I have 2 apples and 5 oranges."
# for match in re.finditer(r"\d+",text):          # iterator of match objects
#  print(match.group(),"at",match.start()) 


        #sub(pattern, repl, string)---------->

# text = "Hello 123, welcome 456!"
# print(re.sub(r"\D","*",text))


        #split
        
# text = "apple, orange; banana, grape"         #Similar to str.split() but with regex power
# print(re.split(r"[;,]",text))

                #meta characters------->

"""               1. Anchors ( ^ and $ )

^ (Start): ^Python matches "Python is fun" but not "I love Python".
$ (End): fun$ matches "I love Python fun" but not "fun times"."""

# import re
# text="python is fun"
# print(re.search(r"^python",text))      #start

# text="I love Python fun"
# print(re.search("fun$",text))          #end


              #2. The Wildcards & Escapes ( . and \ )
#   . (Any character): a.c matches "abc", "aXc", "a 9c".

# import re
# text="how are you rishana"
# print(re.search(r"^how",text))

# text = "rishana"
# print(re.search(r"r.*a", text))

# text="photo.jpg"
# print(re.search(r"\.jpg$",text))

        #3. Sets ( [] )

# import re
# text="mark:506676"
# print(re.search(r"[0-9]",text))             #get one number match

# import re
# text="mark:506676"
# print(re.search(r"[0-9]+",text))            #get all digits


      #4. Quantifiers (, + , {n} , {n,} , {n,m} )

# import re
# text="a,ab,abb,abbb"
# print(re.findall(r"ab*",text))         #0 or more

# import re
# text = "a ab abb abbb"
# print(re.findall(r"ab+", text))         #match 1 or more

# import re
# text = "number is 1234455 "
# print(re.findall(r"\d{3}", text))     #matches exactly 3 digits 

# import re
# text = "number is 12344546 "               #n or more
# print(re.findall(r"\d{7,}", text))  

# import re
# text = "number is 12347513 "
# print(re.findall(r"\d{3,5}", text))     # 3 to 5

# import re
# text = "number is 123475133445 "
# print(re.findall(r"\d[3-5]", text))       # (Range) last must 3,4,5

       #5. Grouping ( () )

# import re
# text = "hahaha"
# print(re.search(r"(ha)+", text))

# Matches "ha" appearing 2 or more times
# text = "hahaha"
# print(re.search(r"(ha){2,}", text))

        #Grouping & Capturing
# import re
# text = "John: 34, Alice: 45, Bob: 23" 
# print(re.findall(r"(\w+): (\d+)",text))    


           #Compiling Regex---------->
# import re           
# pattern=re.compile(r"\d+")           
# text = "123 apples and 456 oranges"
# print(pattern.findall(text))
# print(pattern.findall(text))

# text = "123 apples and 456 oranges"
# print(re.findall(r"\d+",text))           #without compiling
# print(re.findall(r"\d+",text))
# print(re.findall(r"\d+",text))


                 #Regex Flags--------->
#     1. re.IGNORECASE (or re.I )
# import re
# text="HELLO world"                               #Makes the pattern case-insensitive.
# print(re.findall(r"hello",text,re.IGNORECASE))

#     2. re.MULTILINE (or re.M )
# import re
# text = """first line
# second line
# third line"""                              #Treats each line as a separate string.
# print(re.findall(r"^s\w+",text,re.M))

# text = """first line
# second line
# third line"""
# print(re.findall(r"\w+e$",text,re.M))

    #3. re.DOTALL (or re.S )
# import re
# text = "Hello\nWorld" 
# print(re.search(r"Hello.*World",text,re.DOTALL))   

          
                   #Real-Life Uses of Regular Expressions


                #1. Validation (Checking Input)
# import re
# email="user@example.com"
# if re.match(r"^[\w+\.-]+@[\w+\.-]+\.\w+$",email):
#     print("valid email")
# else:
#     print("invalid email")


              #2. Data Cleaning



