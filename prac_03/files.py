# 1.
OutPut_File = "name.txt"
out_file = open("name.txt", "w")
input_name = input("Enter your name: ")
print(input_name, file=out_file)
out_file.close()

# 2.
file = open("name.txt", "r")
out_file.close()
print("Your name is", input_name)

# 3.
newfile_name = "numbers.txt"
read_file = open("numbers.txt", "r")
new_number1 = int(read_file.readline())
new_number2 = int(read_file.readline())
read_file.close()
print("Sum of first two numbers:", int(new_number1 + new_number2))

# 4.
newfile_name2 = "sums.txt"
this_file = open("sums.txt", "r")
sums = 0
for line in this_file:
    inputs = int(line)
    sums += inputs
this_file.close()
print(sums)
