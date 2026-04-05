# slicing   
a= "Shourya"
character_number= a[0:5] #it will print the string from index 0 to 4
#the character number is like "Shourya"
#                              0123456
print(character_number)

print("str1= ", a[0:]) #it will print the whole string
print("str2= ", a[:6]) #it will print the string from 0 to 5
print("str3= ", a[2:5]) #it will print the string from 2 to 4
print("str4= ", a[-4:-1]) #it will print the string from -4 to -2

print("")
#string functions
a= "shourya"
print(str(a).endswith("ya")) #it will check if the string ends with "ya" or not
print(str(a).capitalize()) #it will capitalize the first letter of the string
print(str(a).replace("shourya", "Shourya")) #it will replace the string with the specified value
print(str(a).find("our")) #it will return the index of the first occurrence of the specified value
print(str(a).count("o")) #it will count the number of occurrences of the specified value


#practise
#1st question
name= "Samaksh"
print("the length of the name is: ", len(name))
#2nd question
statement= "Samaksh has infinite $"
print(statement.find("$")) #it will return the index of the first occurrence of the specified value


#conditional staements 
#to apply for license, give vote
age= 18
if(age>=18):
    print("you are eligible for license and vote")
elif(age<18):
    print("you are not eligible for license and vote") 
else:
    print("bhaad me jao")


    #practise
#1st question
number= int(input("enter number: "))

if (number%2==1):
    print("its neither odd, nor even.")
elif (number%2==0):
    print("its an even number.")
else:    print("its an odd number.")
#2nd question
a= 100
b= 200
c= 300
if (a>b and a>c):
    print("a is the greatest number")
elif (b>a and b>c):
    print("b is the greatest number")
else: print("c,",c,"is the greatest number")
#3rd question
x= 10
if (x%7==0):
    print("x is a multiple of 7")
else: print("x isn't a multiple of 7")


#lists in python
my_list= ["doodh", "dahi", "roti", "sabji", "chokha dal"]
print(type(my_list)) #it will print the type of the variable
print(my_list[0]) #it will print the first element of the list
print(my_list[1:4]) #it will print the elements from index 1 to 3
print(my_list[-3:-1]) #it will print the elements from index -3 to -2
print(my_list[0:]) #it will print the whole list


#list slicing
#list slicing is same as string slicing
a= "Shourya, Samaksh"
character_number= a[0:3] #it will print the string from index 0 to 2
print(character_number)

#list methods
my_list= ["doodh", "dahi", "roti", "sabji", "chokha" "dal"]
my_list.append("lassi") #it will add the element at the end of the list
print(my_list)
my_list.sort() #it will sort the list in ascending order
print(my_list)
my_list.reverse() #it will sort the list in descending order
print(my_list)
my_list.insert(6, "paneer") #it will add the element at the specified index
print(my_list)
my_list.remove("sabji")
print(my_list)
my_list.remove("doodh") #it will remove the specified element from the list
print(my_list)
my_list.pop() #it will remove the last element from the list
print(my_list)


#tuples in python
my_tuple= ("doodh", "dahi", "roti", "sabji", "chokha", "dal")
my_tuple.index("sabji") #it will return the index of the specified element
print(my_tuple)
my_tuple.count("doodh") #it will count the number of occurrences of the specified element
print(my_tuple)


#practise
#1st question
movies= []
mov1= input("How To Train Your Dragon")
mov2= input("Aladdin")
mov3= input("Moana")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
#2nd question
list= [1, 2, 3, 2, 1]
copy_list= list.copy() #it will create a copy of the list
copy_list.reverse() #it will reverse the list

if(copy_list==list):
    print("the list is a palindriome")
else: print("the list isn't a palindriome")
#3rd question
grades= ("C", "D", "A", "A", "B", "A")
grades.count("A") #it will count the number of occurrences of "A"
print(grades.count("A"))
#4th question
grades= ["C", "D", "A", "A", "B", "A"]
grades.sort() #it will sort the list in ascending order
print(grades)