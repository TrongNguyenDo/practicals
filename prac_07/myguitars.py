from guitar import Guitar

# constants
CSV_FILE = 'guitars.csv'


def load_file(csv_file):
    """Read file of guitar details, and return a list of guitars"""
    guitars = []
    # Open the file for reading
    in_file = open(csv_file, 'r')
    in_file.readline()
    # File format is like: name,year,cost

    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging
        # year should be an int
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))

        # Add the guitar we've just constructed to the list
        guitars.append(guitar)

    # Close the file as soon as we've finished reading it
    in_file.close()
    return guitars


def input_non_empty_string(tempt):
    input_str = input(tempt).strip()
    while len(input_str) == 0:
        print('Input can not be blank')
    input_str = input(tempt).strip()
    return input_str


def input_positive_int(new_list):
    """Check if the user enter a positive integer or not"""
    valid = False
    input_number = -1
    while not valid:
        try:
            input_number = int(input("Enter a number: "))
            if input_number < 0:
                print("Number must be >= 1")
            elif input_number > len(new_list):
                print("Invalid movies number")
            else:
                valid = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return input_number


def input_positive_float(new_list):
    """Check if the user enter a positive integer or not"""
    valid = False
    input_number = -1
    while not valid:
        try:
            input_number = float(input("Enter a number: "))
            if input_number < 0:
                print("Number must be >= 1")
            elif input_number > len(new_list):
                print("Invalid movies number")
            else:
                valid = True
        except ValueError:
            print("Invalid input; enter a valid number")
    return input_number


def save_guitar(csv_file, guitars):
    try:
        outfile = open(csv_file, 'w')
        for guitar in guitars:
            print(guitar.name + ',' + str(guitar.year) + ',' + str(guitar.cost), file=csv_file)
        print(f'{len(guitars)} guitars saved to {csv_file}')
        outfile.close()
    except IOError:
        print('Error: can not open file')


def main():
    guitars = load_file(CSV_FILE)
    for guitar in guitars:
        print(guitar)

    # After a sort by year
    print("Sort by year:")
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    # ad a new guitar
    name = input_non_empty_string('Enter guitar name:')
    year = input_positive_int('Enter guitar year:')
    cost = input_positive_float('Enter correct guitar price: ')
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)

    # After a sort by year
    print("Sort by year:")
    guitars.sort()
    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
