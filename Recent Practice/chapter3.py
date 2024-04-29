# string
# they are data types
# all are similiar to C++


# Concatenating strings
# a= "prajwal"
# b="pk"
# print(a+b)
# a[3]="t"   will not work, doesnot support iteam assignment but can be accessed
'''
# str Slicing::: 
    a= "prajwal"
    # print(a[0:3]) # start:stop ..works same like in for loop i<3
    # print(a[-1]) #  lstart:stop:step....last character of the string
    print(a[::-1]) # reverses the string with step 1 from back

    # Slicing with skip 
    print(a[0::2]) # skips one char each
 STRINGs are immmutable

# string functions
# 1. len(var_name)
# 2. var_name.endswith("any str")
# 3. var_name.count("anychar or str")
# 4. var_name.capitalize() Caps only the  1st string
# 5.  .find("word") , says where does it lies, ie 1st 
occurance
#6.    .lower or  .upper         : same concept as replace
# 7.   .replace("previous","new word") , replaces all the similar words  : This doesnt changes the original string just gives us  new replaced string i.e IMMUTABLE 
#     .title()      # caps the 1st 
character of every word
#   .center(5,"*") # to add something is 0th and -1th position of the string

# formatted string: f'{name} is my first name {name2} is my last'



letter =  <NAME> 
<DATE>

name= input("enter you name")
date= input("enter you date")
letter= letter.replace("<NAME>",name)
letter=letter.replace("<DATE>",date)
print(letter) 

name= "prajwal  khatiwada  is"
# print(name.count("  "))
# name=name.replace("  "," ")
print(name.title())   #writes as a title capitalizing every word
print(name.capitalize()) 
print(name)

'''
name=input("ENter you name:")
passs = input("Enter you password:")

print("Hey "+ name +" your " + "*" * (len(passs)) + " is " + str(len(passs))+ " long")  #OR
print(f'HEY {name} your {"*"* (len(passs))} is {len(passs)} long') 






