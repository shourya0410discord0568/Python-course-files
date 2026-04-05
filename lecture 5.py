i=5
while i>=1:
    print(i)
    i-=1
print("Done")
print()
i= 1
while i<=5:
    print(i)
    i+=1
print("Done")
print()
#practise
#1
i= 1 #initialization
while i<=100:
    print(i)
    i+=1
print("Done")
print()
#2
i= 100
while i>=1:
    print(i)
    i-=1
print("Done")
print()
#3
n= int(input("enter the number: "))
i= 1
while i<=10:
    print(n*i)
    i+= 1
print()
#4
numbers= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index= 0
while index<len(numbers):
    print(numbers[index])
    index+= 1
print()
#5
nums= (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x= 36

i= 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at index: ", i)
    else:
        print("finding process continues...")
    i+= 1