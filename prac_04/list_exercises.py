numbers = []
for i in range(5):
    valid = False
    while not valid:
        try:
            numbers.append((int(input("Number: "))))
            valid = True
        except ValueError:
            print("Not a number.Please enter a number.")

print("The first number is " + str(numbers[0]))
# f"{numbers[0]}"
print("The last number is " + str(numbers[-1]))
print("The smallest number is " + str(min(numbers)))
print("The largest number is " + str(max(numbers)))
print("The average of the numbers is " + str(sum(numbers) / len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

input_name = input("Enter username:")
if input_name in usernames:
    print("Access granted")
else:
    print("Access denied")
