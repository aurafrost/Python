"""
Area Calculator for circles and triangles
"""
print("Calculator")

option = input("Enter C for Circle or T for Triangle: ")
if(option=="C"):
  radius=float(input("Enter radius: "))
  pi=3.14159
  area=pi*(radius**2)
  print(str(area))
elif(option=='T'):
  base=float(input("Enter base: "))
  height=float(input("Enter height: "))
  area=0.5*base*height
  print(str(area))
else:
  print("Invalid option.")
print("Program exiting")