"""
This program takes three inputs: the user's name, age, and an int which specifies the number of times the response will repeat.
Then it outputs a hello message followed by the user's name, and the year in which the user will turn 100 the given number of times.

"""
from datetime import date

name = input("Enter your name: ")
age = int(input("Enter your age: "))
repeat = int(input("How many responses would you like to see?: "))
difference = 100-age
currentYear = int(date.today().year)
year = currentYear + difference

for x in range (1,repeat+1):
    print("Hello " + name + ". You will turn 100 in the year " + str(year) + ".")