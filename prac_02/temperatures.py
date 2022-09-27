def menu():
    print("C - Convert Celsius to Fahrenheit")
    print("F - Convert Fahrenheit to Celsius")
    print("Q - Quit")


def main():
    menu()

    choice = input("Enter an option: >> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            celsius12 = cel_to(celsius)
            print(celsius12)

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            fahrenheit12 = fa_to(fahrenheit)
            print(fahrenheit12)
        else:
            print("Invalid option")
        menu()
        choice = input(">>> ").upper()


def cel_to(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fa_to(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()
