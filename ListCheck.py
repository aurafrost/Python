"""
This program returns all ints lower than 10 from a given list.
Then it asks the user for an int and checks and returns all numbers from the new list less than the given int.
"""
list = [4,29,-51,16,3,75,199,-20,0,24,8,2] #initial list
print("The initial list is: "+", ".join(str(n) for n in list))

newlist = []
for element in list:
    if element<10:
        newlist.append(element) #adds all ints from list that are less than 10 to newlist
print("The numbers less than 10 are: "+", ".join(str(n) for n in newlist))

check=10 #defaults to 10 to force user to enter an int less than 10
while check>=10: 
    check=int(input("Enter a number less than 10 (negatives are fine too): "))
    if check>=10:
        print("That number is greater than 9. Try again: ")
finallist = []
for element in newlist:
    if element<check:
        finallist.append(element) #adds all ints from newlist that are less than check
print("The numbers less than "+str(check)+" are: "+", ".join(str(n) for n in finallist))