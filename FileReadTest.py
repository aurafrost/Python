my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

# Add your code below!
for i in range(len(my_list)):
  my_file.write(str(my_list[i])+"\n")
my_file.close()