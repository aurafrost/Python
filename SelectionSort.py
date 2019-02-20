"""
This program sorts a list of random ints using selection sort.
Ints are limited to the range 1-100.
Incomplete code.
"""
import random

numcount=int(input("Enter number of desired ints in list: "))
list = [] #list
count = 0
while count<numcount:
    list.append(random.randint(1,101))
    count+=1
print("The initial list is "+", ".join(str(n) for n in list))

count=0
pos=0
while count<numcount:
    min=list[count]
    for element in list:
        if list[count]<min:
            min=list[count]
            pos=element
    temp=list[count]
    list[count]=min
    list[pos]=temp
    count+=1

print("The sorted list is "+", ".join(str(n) for n in list))