             #read-------------------->

# file=open("sample.txt","r")
# content=file.read()                  #reads the entire content
# print(content)
# file.close()

# file=open("sample.txt","r")
# content=file.readline()            #reads one lines
# print(content)
# file.close()

# file=open("sample.txt","r")
# content=file.readlines()        #reads all lines and returns them as a list of strings
# print(content)
# file.close()



               #write------------------------->

# file=open("sample.txt","w")
# content=file.write()                            #writes a single string to the file
# print(content)                                    #there is no file,the write()create new file.
# file.close()

# file=open("sample.txt", "w")
# content=file.writelines(["hello\n","welcome to python\n"])      #writes a list of string to the file
# print(content)
# file.close()

                #appending data-------------->

# file=open("sample.txt","a")
# content=file.write("appended text\n")      #add new content without overwriting its existing content
# file.close()


                 #with statement------------->

# with open("sample.txt","r" )as file:       #with statement automatically close the file
#  content=file.read()
#  print(content)

        #file positioning--------------------->seek and tell

# with open("sample.txt","r")as file:
#  file.read()
#  position= file.tell()
#  print(position)

with open("sample.txt","r")as abc:
    abc.seek(4)
    print(abc.read())

 
 



































































