"""
This program takes two ints as input and outputs whether that first int is negative, 0, even, odd, or an even multiple of 4.
It then divides the first int by the second and 
returns a message depending on whether the first number is evenly divisible by the second and its remainder if any.
"""
num = int(input("Enter a number: ")) #first input
check = int(input("Enter a number to divide by: ")) # second input
if(num<0):
    print("The number "+str(num)+" is not a positive number.")
elif(num==0):
    print("The number is 0.")
elif(num%4==0):
    print("The number "+str(num)+" is even and a multiple of 4.")
elif(num%2==0):
    print("The number "+str(num)+" is an even number.")
else:
    print("The number "+str(num)+" is an odd number.")
    
if(num%check==0):
    print("The number "+str(num)+" is evenly divisible by "+str(check)+".")
else:
    print("The number "+str(num)+" is not evenly divisible by "+str(check)+". The remainder is "+str(num%check)+".")