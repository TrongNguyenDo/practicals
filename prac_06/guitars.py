from guitar import Guitar


def main():
    """Guitar program, using Guitar class."""
    guitar_list = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitar_list.append(new_guitar)
        print(new_guitar, "added.")
        name = input("Name: ")

        guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
        guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
        guitar_list.append(Guitar("Fender Stratocruisers", 2014, 768.40))

        if guitar_list:  # lists, strings and other collections are False when empty, True when non-empty
            # In order for sorting to work on Guitar objects,
            # at least the __lt__ method must be defined in Guitar class
            guitar_list.sort()
            print("These are my guitars:")
            for i, guitar in enumerate(guitar_list, 1):
                vintage_string = ""
                if guitar.is_vintage():
                    vintage_string = " (vintage)"
                # Note the use of the format method and numbered placeholders
                print(
                    "Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
        else:
            print("No guitars :( Quick, go and buy one!")

    main()
