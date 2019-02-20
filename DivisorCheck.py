"""
This program takes an int from the user then returns all divisors of that int from lowest to highest.
"""
num = int(input("Enter an integer: "))
divisorList = []
for x in range(1,num+1):
    if num%x==0:
        divisorList.append(x) #adds x to divisorList if it has no remainder when divided into num
print("The divisors of "+str(num)+" are: "+", ".join(str(n) for n in divisorList))
if(len(divisorList)==2):
    print("The number "+str(num)+" is prime.") #prints this if there're only two elements in divisorList