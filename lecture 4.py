#Dictionaries in python
info= {
    "key": "value",
    "name": "Shourya",
    "learning": "Python",
    "subjects": "Python, Java, JavaScript"
}
print(info["name"])
# print(info["surname"]) #This will give an error because there is no key named surname in the dictionary
info["name"]= "Shourya Pratap" #This will change the value of the key name to Shourya Pratap
info["surnsme"]= "Singh" #This will add a new key named surname with the value Singh to the dictionary
print(info)


#Nested dictionaries
info2= {
    "name": "Shourya",
    "learning": "Python",
    "subjects": {"Python": 80,
                "Java": 70,
                "JavaScript": 60
},
    "address": {
        "city": "Delhi",
        "state": "Delhi",
        "country": "India"
    }
    
}
print(info2)


#Dictionaries methods
info2.keys() #This will return all the keys in the dictionary
info2.values() #This will return all the values in the dictionary
info2.items() #This will return all the key-value pairs in the dictionary as a list of tuples
info.get("key") #This will return the value of the key if it exists in the dictionary, otherwise it will return None
info2.update({"district": "New Delhi"}) #This will add a new key named district with the value New Delhi to the dictionary
print(info2)


#Sets
Collection= {"Charizard", "Blastoise", "Venusar", "Pikachu"}
Collection_type= {"fire", "water", "grass", "electric"}
print(type(Collection)) #This will print the type of the variable Collection which is set
Collection.add("Mewtwo") #This will add a new element Mewtwo to the set
print(Collection)
Collection_type.add("psychic") #This will add a new element psychic to the set
print(Collection_type)
Collection.remove("Pikachu") #This will remove the element Pikachu from the set
print(Collection)
Collection_type.remove("electric") #This will remove the element electric from the set
print(Collection_type)
Collection.pop() #This will remove a random element from the set and return it
print(Collection)
Collection.clear() #This will remove all the elements from the set
print(Collection)
Collection.union(Collection_type) #This will return a new set which is the union of the two sets
Collection.intersection(Collection_type) #This will return a new set which is the intersection of the two sets
print(Collection)


#Practice problems
#1
table= {
    "a piece of furniture"
    "list of facts and figures",
}
cat= {
    "a small animal"
}
#2
classroom= {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
}
print(len(classroom)) #Hence it will give the number of classrooms needed to teach the students
#3
marks= {}

x = int(input("Physics marks: "))
marks.update({"Physics": x})
y= int(input("Chemistry marks: "))
marks.update({"Chemistry": y})
z= int(input("Biology marks: "))
marks.update({"Biology": z})


print(marks)
#4
#first possible solution
set= {9, "9.0"}
print(type(set))
print(set)
#second possible solution
set= {
    ("float", 9.0)
    ("int", 9)
}
print(type(set))
print(set)