"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world." 

print("MAD LIBS")
name=input("Enter a name: ")
adj1=input("Enter adjective 1: ")
adj2=input("Enter adjective 1: ")
adj3=input("Enter adjective 1: ")
verb1=input("Enter a verb: ")
noun1=input("Enter noun 1: ")
noun2=input("Enter noun 2: ")
animal=input("Enter animal: ")
food=input("Enter food: ")
fruit=input("Enter fruit: ")
superhero=input("Enter superhero: ")
country=input("Enter country: ")
dessert=input("Enter dessert: ")
year=input("Enter year: ")
print(STORY % (name,adj1,adj2,animal,food,verb1,noun1,fruit,adj3,name,superhero,name,country,name,dessert,name,year,noun2))