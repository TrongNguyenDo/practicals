"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
name = input("Enter a name: ")


def menu():
    print("(H) Hello")
    print("(G) Goodbye")
    print("(Q) Quit")


menu()
choice = input("Enter an option: >> ").upper()

while choice != 'Q':
    if choice == 'H':
        print("Hello ", name)

    elif choice == 'G':
        print("Goodbye ", name)
    else:
        print("Invalid choice")

    print()
    menu()
    choice = input("Enter an option: >> ").upper()

print("Thank you for using this program :).Have a nice day!")
