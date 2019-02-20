"""
This program checks a string and returns whether or not it is a palindrome.
"""
import math

string = input("Please enter a string: ")
length = len(string)
start = 0
end = length-1
check = True
if length%2==0:
    for i in range(0,int(length/2)):
        if string[start]!=string[end]:
            check = False
        start+=1
        end-=1
else:
    for i in range(0,math.floor(int(length/2))):
        if string[start]!=string[end]:
            check = False
        start+=1
        end-=1
if check==True:
    print("This string "+string+" is a palindrome.")
else:
    print("This string "+string+" is not a palindrome.")